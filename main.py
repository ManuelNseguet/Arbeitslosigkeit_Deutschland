from src.data_loader import load_data
from src.plots import (
    plot_women_vs_men,
    plot_gender_gap,
    plot_overall_trend
)
from src.config import OUTPUT_DIR
from src.utils import ensure_dir

def main():
    ensure_dir(OUTPUT_DIR)
    df = load_data()

    plot_women_vs_men(df)
    plot_gender_gap(df)
    plot_overall_trend(df)

if __name__ == "__main__":
    main()
