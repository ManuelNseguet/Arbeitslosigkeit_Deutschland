import pandas as pd
from src.config import DATA_PATH

def load_data():
    df = pd.read_csv(DATA_PATH)

    # Einheitliche Spaltennamen
    df.columns = ["Year", "Region", "Gender", "Unemployment"]

    # Pivot: Women / Men als Spalten
    pivot = df.pivot(index="Year", columns="Gender", values="Unemployment").reset_index()

    # Gender Gap
    pivot["GenderGap"] = pivot["Women"] - pivot["Men"]

    # Gesamtwert (Mittelwert)
    pivot["Total"] = (pivot["Women"] + pivot["Men"]) / 2

    return pivot
