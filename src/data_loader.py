import pandas as pd
from src.config import DATA_PATH

def load_data():
    """
    Load unemployment data from CSV and perform basic validation.
    """
    df = pd.read_csv(DATA_PATH)

    required_columns = {"year", "region", "gender", "unemployment_rate"}
    if not required_columns.issubset(df.columns):
        raise ValueError("CSV file is missing required columns.")

    return df
