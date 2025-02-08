import streamlit as st
import pandas as pd

# Load AI-generated trades
ai_trades_df = pd.read_csv("ai_recommendations.csv")

# App Title
st.title("AI-Powered Options Scanner 🚀")

# Display AI-generated trades
st.subheader("AI Trade Recommendations")
st.dataframe(ai_trades_df)

# Add a button to send Telegram alerts
if st.button("Send Telegram Alert"):
    import telegram_alert
    st.success("Trade alerts sent to Telegram!")
