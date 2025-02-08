import openai
import pandas as pd
import json

# Load the option chain data
df = pd.read_csv("option_chain.csv")

# OpenAI API Key (Replace with your key)
openai.api_key = "your_openai_api_key"

def ai_filter_options(df):
    options_data = df.to_string()

    # ChatGPT Prompt
    prompt = f"""
    You are an AI trading assistant. Analyze the following option chain data and select 
    the best option trades based on:
    - High Probability of Profit (Delta between 0.3 - 0.7)
    - Low IV Rank (to avoid IV crush)
    - High Open Interest for liquidity

    Here is the options data:
    {options_data}

    Return the best trade recommendations in JSON format with Strike Price, Type (Call/Put), and Reason.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial analyst."},
                  {"role": "user", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

# Get AI-Filtered Trades
ai_recommendations = ai_filter_options(df)

# Convert AI output to JSON and save
ai_trades_json = json.loads(ai_recommendations)
ai_trades_df = pd.DataFrame(ai_trades_json)

# Save AI recommendations
ai_trades_df.to_csv("ai_recommendations.csv", index=False)

print(ai_trades_df)
