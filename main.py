from src.data_loader import load_data
from src.plots import (
    plot_women_vs_men,
    plot_gender_gap,
    plot_overall_trend
)
from src.config import OUTPUT_DIR

def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    df = load_data()

    plot_women_vs_men(df)
    plot_gender_gap(df)
    plot_overall_trend(df)

    print("All visualizations have been successfully created.")


if __name__ == "__main__":
    main()
