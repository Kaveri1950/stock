import streamlit as st

st.set_page_config(
    page_title="Trading Guide",
    layout="wide"
)

# ---------- Custom Styling ---------- #
st.markdown("""
<style>

.stApp {
    background-color: #f5f7fb;
}

/* Main Title */
.main-title {
    font-size:100px;
    font-weight:1000;
    text-align:center;
    color:#1a1a1a;
    margin-bottom:10px;
}

/* Subtitle */
.subtitle {
    font-size:22px;
    text-align:center;
    color:#555;
    margin-bottom:30px;
}

/* Section title */
.section-title {
    font-size:34px;
    font-weight:700;
    color:#1a1a1a;
}

/* Feature Cards */
.card {
    background-color:white;
    padding:25px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.08);
    border:1px solid #ececec;
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


# ---------- Header ---------- #

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
<p style='text-align:center;color:#888;font-size:14px'>
Built with Streamlit • Stock Analytics Project
</p>
""",
unsafe_allow_html=True
)