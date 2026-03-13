import streamlit as st

st.set_page_config(
    page_title="Trading Guide",
    layout="wide"
)

# ---------- Custom Styling ---------- #
st.markdown("""
<style>

/* Page background */
.stApp {
    background-color: #eef2f7;
}

/* Hero Title */
.main-title {
    font-size:120px;
    font-weight:900;
    text-align:center;
    color:#111;
    margin-top:120px;
    margin-bottom:10px;
}

/* Subtitle */
.subtitle {
    font-size:24px;
    text-align:center;
    color:#555;
    margin-bottom:60px;
}

/* Section title */
.section-title {
    font-size:34px;
    font-weight:700;
    color:#111;
}

/* Feature Cards */
.card {
    background-color:#ffffff;
    padding:28px;
    border-radius:14px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    border:1px solid #e6e9ef;
}

.card-title {
    font-size:20px;
    font-weight:600;
    margin-bottom:10px;
}

.card-text {
    color:#555;
    font-size:16px;
}

</style>
""", unsafe_allow_html=True)


# ---------- HERO SECTION ---------- #

st.markdown('<p class="main-title">Trading Guide</p>', unsafe_allow_html=True)

st.markdown(
"""
<p class="subtitle">
A platform to analyze stocks, forecast trends, and understand investment risk before making financial decisions.
</p>
""",
unsafe_allow_html=True)

st.image("app.png", use_container_width=True)

st.markdown("---")


# ---------- Features Section ---------- #

st.markdown('<p class="section-title">Platform Features</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card">
        <div class="card-title">Stock Information</div>
        <div class="card-text">
        Explore historical stock prices, company information, and key financial indicators
        to better understand stock performance.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">Stock Prediction</div>
        <div class="card-text">
        Forecast the next 30 days of stock prices using historical data
        and time-series prediction models.
        </div>
    </div>
    """, unsafe_allow_html=True)


with col2:

    st.markdown("""
    <div class="card">
        <div class="card-title">CAPM Expected Return</div>
        <div class="card-text">
        Estimate expected stock returns using the Capital Asset Pricing Model
        and evaluate risk-adjusted investment opportunities.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <div class="card-title">CAPM Beta Analysis</div>
        <div class="card-text">
        Measure stock volatility relative to the market and understand
        how risky an asset is compared to market movements.
        </div>
    </div>
    """, unsafe_allow_html=True)


st.markdown("---")


# ---------- Footer ---------- #

st.markdown(
"""
<p style='text-align:center;color:#777;font-size:14px'>
Built with Streamlit • Stock Analytics Project
</p>
""",
unsafe_allow_html=True
)