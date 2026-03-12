# Stock Trading Analysis Platform

A comprehensive, interactive web application for stock market analysis, technical indicator visualization, and AI-powered price forecasting. Built with Streamlit, this platform provides professional-grade trading analytics in an accessible interface.

# Live App:
https://stock-trading-analysis-itsw7zcwgwvtdciwp7aed4.streamlit.app/

## Features

### Stock Analysis Dashboard
- **Real-time Data**: Live stock data via Yahoo Finance API
- **Company Insights**: Sector information, employee count, financial metrics
- **Interactive Charts**: Candlestick and Line charts with customizable timeframes (1D, 5D, 1M, 6M, YTD, 1Y, 5Y, Max)
- **Technical Indicators**: RSI, MACD, Moving Averages with overbought/oversold signals
- **Key Metrics**: Market Cap, Beta, P/E Ratio, Profit Margins, Quick Ratio, Revenue Growth

### AI Price Prediction
- **Time Series Forecasting**: ARIMA model for 30-day price predictions
- **Model Performance**: RMSE score evaluation (typically 0.2-0.94 range)
- **Visual Forecasts**: Side-by-side comparison of actual vs predicted prices
- **Model Validation**: Walk-forward validation and backtesting

### CAPM & Comparative Analysis
- **CAPM Calculations**: Beta coefficients and expected returns
- **Multi-Stock Comparison**: Normalized returns across different stocks
- **Risk Assessment**: Investment risk analysis and portfolio insights
- **Performance Metrics**: Cumulative returns and volatility analysis

## Installation & Local Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kaveri1950/Stock-trading-analysis.git
   cd Stock-trading-analysis

2.  Navigate to the project directory and start the Streamlit app by running the following on terminal:
    ```bash
    streamlit run stock.py.

