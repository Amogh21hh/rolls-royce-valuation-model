"""
Project Osprey — Rolls-Royce Holdings plc (LSE: RR.)
Interactive DCF Valuation Dashboard

Reads the FCF projections from the linked Excel model and re-runs the DCF
in real time as the user adjusts WACC and terminal growth via sidebar sliders.

Run locally:
    pip install streamlit pandas openpyxl plotly
    streamlit run app.py
"""

from pathlib import Path

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# ----------------------------------------------------------------------------
# Page config
# ----------------------------------------------------------------------------
st.set_page_config(
    page_title="Project Osprey — RR. DCF",
    page_icon=":chart_with_upwards_trend:",
    layout="wide",
)

# Locate the workbook one directory up from this file
MODEL_PATH = Path(__file__).resolve().parent.parent / "02_Financial_Models" / "RR_LBO_DCF_Model.xlsx"

# Static fallbacks if the workbook cannot be read (keeps the dashboard usable)
FALLBACK_FCF = {
    "2025A": 3.30,
    "2026E": 3.70,
    "2027E": 4.40,
    "2028E": 5.15,
    "2029E": 5.45,
    "2030E": 5.70,
}
FALLBACK_NET_CASH = 1.90       # £bn, 31-Dec-2025
FALLBACK_SHARES = 8.30         # bn shares outstanding
FALLBACK_PRICE_P = 1208.20     # pence, spot 21-May-26

# Discount periods (mid-year convention, valuation date 23-May-2026)
DISCOUNT_PERIODS = {
    "2026E": 0.6,
    "2027E": 1.5,
    "2028E": 2.5,
    "2029E": 3.5,
    "2030E": 4.5,
}


# ----------------------------------------------------------------------------
# Data loading
# ----------------------------------------------------------------------------
@st.cache_data(show_spinner=False)
def load_inputs(model_path: Path) -> dict:
    """Read FCF projections, net cash, shares, and spot price from the model."""
    if not model_path.exists():
        return {
            "fcf": FALLBACK_FCF.copy(),
            "net_cash": FALLBACK_NET_CASH,
            "shares": FALLBACK_SHARES,
            "price_p": FALLBACK_PRICE_P,
            "source": "fallback (workbook not found at expected path)",
        }

    try:
        # Read the raw Assumptions tab; columns are positional in this template
        asm = pd.read_excel(
            model_path,
            sheet_name="Assumptions",
            header=None,
            engine="openpyxl",
        )

        # Row 13 (0-indexed 12) holds the FCF series; cols C..H = 2025A..2030E
        labels = ["2025A", "2026E", "2027E", "2028E", "2029E", "2030E"]
        fcf_series = {}
        for i, label in enumerate(labels):
            value = asm.iat[12, 2 + i]
            fcf_series[label] = float(value)

        net_cash = float(asm.iat[31, 2])   # Row 32 col C
        shares = float(asm.iat[30, 2])     # Row 31 col C
        price_p = float(asm.iat[32, 2])    # Row 33 col C

        return {
            "fcf": fcf_series,
            "net_cash": net_cash,
            "shares": shares,
            "price_p": price_p,
            "source": str(model_path.name),
        }

    except Exception as exc:  # noqa: BLE001 — surface to UI
        st.warning(f"Could not read workbook ({exc}); using static fallbacks.")
        return {
            "fcf": FALLBACK_FCF.copy(),
            "net_cash": FALLBACK_NET_CASH,
            "shares": FALLBACK_SHARES,
            "price_p": FALLBACK_PRICE_P,
            "source": "fallback (read error)",
        }


# ----------------------------------------------------------------------------
# DCF engine
# ----------------------------------------------------------------------------
def run_dcf(fcf: dict, wacc: float, g: float, net_cash: float, shares: float) -> dict:
    """Return PV explicit, PV terminal, EV, equity, implied price (pence)."""
    if wacc <= g:
        return {
            "pv_explicit": float("nan"),
            "pv_terminal": float("nan"),
            "ev": float("nan"),
            "equity": float("nan"),
            "implied_p": float("nan"),
            "error": "WACC must exceed terminal growth (g).",
        }

    # PV of explicit forecast 2026-2030
    explicit_fcfs = {y: fcf[y] for y in ["2026E", "2027E", "2028E", "2029E", "2030E"]}
    pv_explicit = sum(
        cf / (1 + wacc) ** DISCOUNT_PERIODS[y] for y, cf in explicit_fcfs.items()
    )

    # Terminal value (Gordon Growth), discounted at last explicit period
    fcf_2030 = fcf["2030E"]
    terminal_value = fcf_2030 * (1 + g) / (wacc - g)
    pv_terminal = terminal_value / (1 + wacc) ** DISCOUNT_PERIODS["2030E"]

    ev = pv_explicit + pv_terminal
    equity = ev + net_cash
    implied_pounds = equity / shares
    implied_p = implied_pounds * 100  # convert £ to pence

    return {
        "pv_explicit": pv_explicit,
        "pv_terminal": pv_terminal,
        "ev": ev,
        "equity": equity,
        "implied_p": implied_p,
        "error": None,
    }


# ----------------------------------------------------------------------------
# UI
# ----------------------------------------------------------------------------
def main() -> None:
    inputs = load_inputs(MODEL_PATH)

    # Header
    st.markdown(
        """
        <div style="background:#1F3864;padding:18px 24px;border-radius:6px;margin-bottom:18px">
          <div style="color:#FFFFFF;font-size:11px;letter-spacing:2px;font-weight:600">PROJECT OSPREY</div>
          <div style="color:#FFFFFF;font-size:26px;font-weight:700">Rolls-Royce Holdings plc — DCF Sandbox</div>
          <div style="color:#CADCFC;font-size:13px;font-style:italic">LSE: RR.  |  Valuation date 23-May-2026</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----- Sidebar -----
    st.sidebar.header("Valuation Drivers")
    st.sidebar.caption("Adjust to re-run the DCF in real time.")

    wacc_pct = st.sidebar.slider(
        "WACC / Cost of Equity (%)",
        min_value=6.0,
        max_value=14.0,
        value=9.5,
        step=0.1,
        help="Weighted average cost of capital. Base case 9.5%.",
    )

    g_pct = st.sidebar.slider(
        "Terminal Growth Rate (%)",
        min_value=1.0,
        max_value=4.0,
        value=2.25,
        step=0.05,
        help="Perpetual growth applied to FY30 FCF. Base case 2.25%.",
    )

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Static inputs (from model)**")
    st.sidebar.write(f"Net cash: £{inputs['net_cash']:.2f}bn")
    st.sidebar.write(f"Shares outstanding: {inputs['shares']:.2f}bn")
    st.sidebar.write(f"Current price: {inputs['price_p']:.0f}p")
    st.sidebar.caption(f"Source: {inputs['source']}")

    # ----- Calculation -----
    result = run_dcf(
        fcf=inputs["fcf"],
        wacc=wacc_pct / 100,
        g=g_pct / 100,
        net_cash=inputs["net_cash"],
        shares=inputs["shares"],
    )

    if result["error"]:
        st.error(result["error"])
        return

    upside = result["implied_p"] / inputs["price_p"] - 1

    # ----- KPI row -----
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="IMPLIED SHARE PRICE",
            value=f"{result['implied_p']:,.0f}p",
            delta=f"{upside * 100:+.1f}% vs spot",
            delta_color="normal",
        )
    with c2:
        st.metric("Enterprise Value", f"£{result['ev']:,.1f}bn")
    with c3:
        st.metric("Equity Value", f"£{result['equity']:,.1f}bn")
    with c4:
        st.metric("Current Price", f"{inputs['price_p']:,.0f}p")

    # Headline call-out
    if upside >= 0.15:
        verdict, colour = "BUY — material upside", "#2E8B57"
    elif upside >= -0.05:
        verdict, colour = "HOLD — fair value range", "#C9A961"
    else:
        verdict, colour = "TRIM / SELL — overvalued", "#B0413E"

    st.markdown(
        f"""
        <div style="background:{colour};color:#FFFFFF;padding:14px 20px;
                    border-radius:6px;margin:14px 0;font-weight:600;font-size:16px">
          {verdict}  &nbsp;|&nbsp;  Implied {result['implied_p']:,.0f}p  vs  Spot {inputs['price_p']:,.0f}p
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----- Cash flow line chart -----
    st.subheader("Free Cash Flow Trajectory (£bn)")

    fcf_df = pd.DataFrame(
        {"Year": list(inputs["fcf"].keys()), "FCF": list(inputs["fcf"].values())}
    )

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=fcf_df["Year"],
            y=fcf_df["FCF"],
            mode="lines+markers+text",
            line=dict(color="#1F3864", width=3),
            marker=dict(size=11, color="#C9A961", line=dict(color="#1F3864", width=2)),
            text=[f"£{v:.2f}bn" for v in fcf_df["FCF"]],
            textposition="top center",
            textfont=dict(size=11, color="#1F3864"),
            name="FCF",
            hovertemplate="%{x}<br>FCF: £%{y:.2f}bn<extra></extra>",
        )
    )
    # Highlight management 2028 corridor (£5.0–5.3bn)
    fig.add_hrect(
        y0=5.0, y1=5.3,
        fillcolor="#C9A961", opacity=0.12,
        layer="below", line_width=0,
        annotation_text="2028 mgmt corridor £5.0–5.3bn",
        annotation_position="top left",
        annotation=dict(font_color="#5A5F6E", font_size=10),
    )
    fig.update_layout(
        height=420,
        margin=dict(l=30, r=30, t=30, b=30),
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        yaxis=dict(title="FCF (£bn)", gridcolor="#E5E7EB", zerolinecolor="#D1D5DB"),
        xaxis=dict(showgrid=False),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True)

    # ----- Bridge breakdown -----
    st.subheader("Valuation Bridge")
    bridge_df = pd.DataFrame(
        {
            "Component": [
                "Sum of PV (2026-2030 FCF)",
                "PV of Terminal Value",
                "Enterprise Value",
                "(+) Net Cash",
                "Equity Value",
                "÷ Shares Outstanding (bn)",
                "= Implied Share Price",
            ],
            "Value": [
                f"£{result['pv_explicit']:,.2f}bn",
                f"£{result['pv_terminal']:,.2f}bn",
                f"£{result['ev']:,.2f}bn",
                f"£{inputs['net_cash']:,.2f}bn",
                f"£{result['equity']:,.2f}bn",
                f"{inputs['shares']:,.2f}",
                f"{result['implied_p']:,.0f}p",
            ],
        }
    )
    st.dataframe(bridge_df, use_container_width=True, hide_index=True)

    # ----- Footer -----
    st.markdown("---")
    st.caption(
        "Internal valuation tool. Inputs sourced from RR Holdings FY25 results "
        "(26-Feb-2026). Not for external distribution. Built on the same DCF "
        "mechanics as RR_LBO_DCF_Model.xlsx."
    )


if __name__ == "__main__":
    main()
