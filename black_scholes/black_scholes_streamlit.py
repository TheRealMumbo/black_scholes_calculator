import streamlit as st
import os
import black_scholes_engine as bse

# add these imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


st.title("BLACK SCHOLES EUROPEAN OPTION CALCULATOR", text_alignment="center")

s0 = st.number_input(
    "Current stock price:",
    min_value=0.001,
    value=100.00
)
x = st.number_input(
    "Strike price:",
    min_value=0.001,
    value=100.00
)
r = st.number_input(
    "Risk free interest rate:",
    min_value=0.001,
    value=0.01
)
q = st.number_input(
    "Dividends, if 0 enter 0 please:",
)
t = st.number_input(
    "Time until strike:",
    min_value=0.001,
    value=0.1
)
sigma = st.number_input(
    "Annualized volatility of stock:",
    min_value=0.001,
    value=0.1
)

col1, col2 = st.columns([2, 1])

with col1:
    if st.button("Calculate European Call Price"):
        st.write(bse.calc_european_call_option(s0, x, r, q, t, sigma))

with col2:
    if st.button("Calculate European Put Price"):
        st.write(bse.calc_european_put_option(s0, x, r, q, t, sigma))


# --------------------------
# Heatmaps (extension)
# --------------------------
st.divider()
st.subheader("Option Price Heatmaps")

with st.expander("Heatmap parameters", expanded=True):
    hcol1, hcol2 = st.columns(2)

    with hcol1:
        min_spot = st.number_input("Min spot price", min_value=0.001, value=80.00)
        max_spot = st.number_input("Max spot price", min_value=0.001, value=120.00)
        spot_steps = st.slider("Spot steps", min_value=5, max_value=25, value=10)

    with hcol2:
        min_vol = st.number_input("Min volatility (σ)", min_value=0.001, value=0.10)
        max_vol = st.number_input("Max volatility (σ)", min_value=0.001, value=0.30)
        vol_steps = st.slider("Vol steps", min_value=5, max_value=25, value=10)

    show_values = st.checkbox("Show values on heatmap (slower for big grids)", value=True)

# quick sanity checks (avoid weird input combos)
if max_spot <= min_spot:
    st.warning("Max spot price must be greater than min spot price.")
elif max_vol <= min_vol:
    st.warning("Max volatility must be greater than min volatility.")
else:
    spots = np.linspace(min_spot, max_spot, spot_steps)
    vols = np.linspace(min_vol, max_vol, vol_steps)

    def build_price_grid(kind: str) -> pd.DataFrame:
        grid = np.zeros((len(vols), len(spots)), dtype=float)

        for i, vol in enumerate(vols):
            for j, s in enumerate(spots):
                if kind == "call":
                    grid[i, j] = bse.calc_european_call_option(s, x, r, q, t, vol)
                else:
                    grid[i, j] = bse.calc_european_put_option(s, x, r, q, t, vol)

        df = pd.DataFrame(
            grid,
            index=np.round(vols, 4),
            columns=np.round(spots, 2),
        )
        df.index.name = "Volatility (σ)"
        df.columns.name = "Spot Price"
        return df

    def plot_heatmap(df: pd.DataFrame, title: str):
        fig, ax = plt.subplots()
        im = ax.imshow(df.values, aspect="auto", origin="lower")

        ax.set_title(title)
        ax.set_xlabel(df.columns.name or "")
        ax.set_ylabel(df.index.name or "")

        ax.set_xticks(range(len(df.columns)))
        ax.set_xticklabels(df.columns, rotation=45, ha="right")

        ax.set_yticks(range(len(df.index)))
        ax.set_yticklabels(df.index)

        cbar = fig.colorbar(im, ax=ax)
        cbar.ax.set_ylabel("Option Price", rotation=90)

        if show_values:
            # keep it readable: smaller font when grid gets bigger
            font_size = 9 if (df.shape[0] <= 12 and df.shape[1] <= 12) else 7
            for i in range(df.shape[0]):
                for j in range(df.shape[1]):
                    ax.text(
                        j, i,
                        f"{df.iat[i, j]:.2f}",
                        ha="center", va="center",
                        fontsize=font_size
                    )

        fig.tight_layout()
        return fig

    if st.button("Generate heatmaps"):
        call_df = build_price_grid("call")
        put_df = build_price_grid("put")

        c1, c2 = st.columns(2)
        with c1:
            st.pyplot(plot_heatmap(call_df, "CALL"))
        with c2:
            st.pyplot(plot_heatmap(put_df, "PUT"))

        # optional: let people inspect numbers
        with st.expander("Raw tables"):
            st.write("Call prices")
            st.dataframe(call_df)
            st.write("Put prices")
            st.dataframe(put_df)
