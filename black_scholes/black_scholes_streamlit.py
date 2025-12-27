<<<<<<< HEAD
import streamlit as st
import os
import black_scholes_engine as bse


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
=======
import streamlit as st
import os
import black_scholes_engine as bse


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
>>>>>>> 89a4cea2261ab5472e797eb1d5a1d663a706aafb
