import matplotlib.pyplot as plt
from src.config import (
    FIG_SIZE,
    DPI,
    COLOR_WOMEN,
    COLOR_MEN,
    OUTPUT_DIR
)
from src.utils import prepare_gender_pivot, calculate_gender_gap


def plot_women_vs_men(df):
    data = prepare_gender_pivot(df)

    plt.figure(figsize=FIG_SIZE)
    plt.plot(data["year"], data["Women"], label="Women", color=COLOR_WOMEN)
    plt.plot(data["year"], data["Men"], label="Men", color=COLOR_MEN)

    plt.title("Unemployment Rate in North Bavaria by Gender")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")
    plt.legend()
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "01_women_vs_men.png", dpi=DPI)
    plt.close()


def plot_gender_gap(df):
    gap = calculate_gender_gap(df)

    plt.figure(figsize=FIG_SIZE)
    plt.bar(gap["year"], gap["Gender Gap"], color="#999999")

    plt.axhline(0, linewidth=1)
    plt.title("Gender Gap in Unemployment Rate (Women − Men)")
    plt.xlabel("Year")
    plt.ylabel("Difference in percentage points")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "02_gender_gap.png", dpi=DPI)
    plt.close()


def plot_overall_trend(df):
    overall = df.groupby("year")["unemployment_rate"].mean().reset_index()

    plt.figure(figsize=FIG_SIZE)
    plt.plot(overall["year"], overall["unemployment_rate"])

    plt.title("Overall Unemployment Trend in North Bavaria")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")
    plt.tight_layout()

    plt.savefig(OUTPUT_DIR / "03_overall_trend.png", dpi=DPI)
    plt.close()

    
