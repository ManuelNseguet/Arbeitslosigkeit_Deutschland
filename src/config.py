from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parents[1]

# Paths
DATA_PATH = BASE_DIR / "data" / "raw" / "Arbeitslosigkeit_maenner_frauen.csv"
OUTPUT_DIR = BASE_DIR / "outputs"

# Plot settings
FIG_SIZE = (8, 5)
DPI = 300

# Colorblind-friendly colors
COLOR_WOMEN = "#E69F00"
COLOR_MEN = "#0072B2"
