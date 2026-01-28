import matplotlib.pyplot as plt
from src.config import FIG_SIZE, DPI, COLOR_WOMEN, COLOR_MEN, OUTPUT_DIR

def plot_women_vs_men(df):
    plt.figure(figsize=FIG_SIZE)
    plt.plot(df["Year"], df["Women"], label="Women", color=COLOR_WOMEN)
    plt.plot(df["Year"], df["Men"], label="Men", color=COLOR_MEN)

    plt.title("Unemployment Rate in Northern Bavaria by Gender (2018–2023)")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")
    plt.legend()
    plt.figtext(0.5, -0.15, "Source: INKAR (BBSR)", ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "01_women_vs_men.png", dpi=DPI)
    plt.close()


def plot_gender_gap(df):
    plt.figure(figsize=FIG_SIZE)
    plt.plot(df["Year"], df["GenderGap"], color="black")

    plt.title("Gender Gap in Unemployment (Women − Men) in Northern Bavaria")
    plt.xlabel("Year")
    plt.ylabel("Difference (percentage points)")
    plt.axhline(0)
    plt.figtext(0.5, -0.15, "Source: INKAR (BBSR)", ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "02_gender_gap_", dpi=DPI)
    plt.close()


def plot_overall_trend(df):
    plt.figure(figsize=FIG_SIZE)
    plt.plot(df["Year"], df["Total"], color="gray")

    plt.title("Overall Unemployment Rate in Northern Bavaria (2018–2023)")
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate (%)")
    plt.figtext(0.5, -0.15, "Source: INKAR (BBSR)", ha="center", fontsize=9)

    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "03_overall_trend.png", dpi=DPI)
    plt.close()
