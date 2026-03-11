import pandas as pd

def transform_data():

    print("Transforming data...")

    # Load raw extracted data
    df = pd.read_csv("data/extracted/raw_diabetes_data.csv")

    # Remove duplicates
    df = df.drop_duplicates()

    # Standardize column names
    df.columns = df.columns.str.lower().str.replace(" ", "_")

    # Handle missing values
    df = df.dropna()

    # Run simple EDA
    print("Summary Statistics:")
    print(df.describe())

    print("\nMissing Values:")
    print(df.isnull().sum())

    # Save cleaned data
    df.to_csv("data/transformed/clean_diabetes_data.csv", index=False)

    print("Cleaned data saved to data/transformed")

    return df
