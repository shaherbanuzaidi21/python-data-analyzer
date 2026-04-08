import pandas as pd

def analyze_data(file):
    df = pd.read_csv(file)

    print("First 5 rows:")
    print(df.head())

    print("\nSummary:")
    print(df.describe())

if __name__ == "__main__":
    analyze_data("data.csv")