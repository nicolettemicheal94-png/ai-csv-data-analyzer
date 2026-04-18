import pandas as pd
import matplotlib.pyplot as plt

print("AI CSV Data Analyzer")

# Upload CSV
file_path = input("Enter CSV file path: ")
df = pd.read_csv(file_path)

print("\nData Preview:")
print(df.head())

# Data cleaning
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

print("\nData cleaned successfully!")

# Query input
query = input("\nEnter your query (average/sum/plot): ").lower()

if "average" in query:
    col = input("Enter column name: ")
    print("Average:", df[col].mean())

elif "sum" in query:
    col = input("Enter column name: ")
    print("Sum:", df[col].sum())

elif "plot" in query:
    x = input("Enter X column: ")
    y = input("Enter
