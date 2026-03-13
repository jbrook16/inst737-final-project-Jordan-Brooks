import pandas as pd
def extract_data():
    """
    Extracts the diabetes mortality dataset from the source CSV file
    and stores the raw data.

    Returns
    -------
    pandas.DataFrame
        Raw dataset loaded from the source file.
    """


def extract_data():

    print("Extracting data...")

    df = pd.read_csv("HDPulse_data_export.csv", skiprows=3)

    # Save raw data
    df.to_csv("data/extracted/raw_diabetes_data.csv", index=False)

    print("Raw data saved to data/extracted")

    return df
