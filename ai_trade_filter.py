import pandas as pd
import os

filename = "option_chain.csv"

# Ensure the file exists before reading
if not os.path.exists(filename):
    print(f"Error: {filename} not found! Ensure fetch_option.py runs successfully before this.")
else:
    df = pd.read_csv(filename)
    print("Option chain data successfully loaded:")
    print(df.head(10))

df.to_csv("ai_recommendations.csv", index=False)
print("AI recommendations saved to ai_recommendations.csv")
