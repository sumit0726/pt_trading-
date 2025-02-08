import pandas as pd
import os

file_path = "ai_recommendations.csv"  # Change this to full path if needed

if os.path.exists(file_path):
    ai_trades_df = pd.read_csv(file_path)
    print("File loaded successfully!")
else:
    print(f"Error: {file_path} not found. Please generate or place the file in the correct directory.")
