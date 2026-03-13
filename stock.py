import streamlit as st

# Page config
st.set_page_config(
    page_title="Trading Guide App",
    layout="wide"
)

# Custom CSS for styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #eef2f7, #ffffff);
}

.big-title {
    font-size: 70px;
    font-weight: 800;
    text-align: center;
    color: #1f2937;
    margin-top: 20px;
}

.subtitle {
    font-size: 22px;
    text-align: center;
    color: #4b5563;
    margin-bottom: 40px;
}

.feature-card {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.08);
    text-align: center;
}

.feature-title {
    font-size: 22px;
    font-weight: 700;
}

.feature-text {
    font-size: 16px;
    color: #555;
}

</style>
""", unsafe_allow_html=True)


# BIG HEADLINE
st.markdown('<p class="big-title">Trading Guide Platform</p>', unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">A smart platform to analyze stocks, predict prices, and evaluate investment risk before making decisions.</p>',
    unsafe_allow_html=True
)

st.image("app.png", use_container_width=True)

st.markdown("## Platform Features")

# Feature columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📊 Stock Information</div>
        <div class="feature-text">
        Explore detailed company and stock market information to understand performance and trends.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📈 Stock Prediction</div>
        <div class="feature-text">
        Forecast future closing prices using historical stock data and predictive models.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">💰 CAPM Return</div>
        <div class="feature-text">
        Estimate expected stock returns using the Capital Asset Pricing Model.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="feature-card">
        <div class="feature-title">📉 CAPM Beta</div>
        <div class="feature-text">
        Measure the risk of individual stocks relative to the overall market.
        </div>
    </div>
    """, unsafe_allow_html=True)