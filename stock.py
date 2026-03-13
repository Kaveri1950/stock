import streamlit as st

st.set_page_config(
    page_title="Trading Guide App",
    page_icon="📈",
    layout="wide"
)

# ---------------- HERO SECTION ---------------- #

st.markdown("""
<h1 style='text-align:center; color:#1f77b4; font-size:48px;'>
📈 Trading Guide
</h1>
<p style='text-align:center; font-size:20px; color:gray;'>
A data-driven platform to analyze stocks, forecast trends,
and evaluate investment risk before making financial decisions.
</p>
""", unsafe_allow_html=True)

st.image("app.png", use_container_width=True)

st.markdown("---")


# ---------------- FEATURES SECTION ---------------- #

st.markdown(
"""
<h2 style='text-align:center;'>Platform Features</h2>
<p style='text-align:center; color:gray;'>Tools designed to help you make smarter investment decisions.</p>
""",
unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="📊 Stock Information", value="Real-time Insights")
    st.write("Access historical prices, company data, and market indicators to understand stock performance.")

with col2:
    st.metric(label="📈 Stock Prediction", value="30-Day Forecast")
    st.write("Predict future stock prices using machine learning models trained on historical market data.")

with col3:
    st.metric(label="💰 CAPM Expected Return", value="Risk-Adjusted")
    st.write("Estimate expected returns based on market risk using the Capital Asset Pricing Model.")

with col4:
    st.metric(label="⚖️ CAPM Beta", value="Volatility Analysis")
    st.write("Measure how sensitive a stock is to market movements and evaluate investment risk.")


st.markdown("---")


# ---------------- WHY USE THIS APP ---------------- #

st.markdown(
"""
<h2 style='text-align:center;'>Why Use This Platform?</h2>
""",
unsafe_allow_html=True
)

c1, c2 = st.columns(2)

with c1:
    st.markdown("### 📉 Data-Driven Decisions")
    st.write("Leverage analytics and predictive models to support informed investment strategies.")

    st.markdown("### 📊 Interactive Visualizations")
    st.write("Explore stock trends with intuitive charts and financial indicators.")

with c2:
    st.markdown("### ⚡ Fast Market Insights")
    st.write("Quickly analyze stocks and compare potential investment opportunities.")

    st.markdown("### 🧠 Risk & Return Analysis")
    st.write("Evaluate the relationship between risk and expected returns before investing.")


st.markdown("---")


# ---------------- CALL TO ACTION ---------------- #

st.markdown(
"""
<h3 style='text-align:center;'>Start Exploring Stocks Today 🚀</h3>
<p style='text-align:center; color:gray;'>
Navigate through the sidebar to explore stock analytics, forecasts,
and risk evaluation tools.
</p>
""",
unsafe_allow_html=True
)


# ---------------- FOOTER ---------------- #

st.markdown(
"""
<hr>
<p style='text-align:center; color:gray; font-size:14px;'>
Built with Streamlit • Data Analytics Project
</p>
""",
unsafe_allow_html=True
)