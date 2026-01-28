## 📊 Geschlechterunterschiede bei der Arbeitslosigkeit in Nordbayern

This project analyzes gender-specific differences in unemployment rates in selected
regions of **North Bavaria (Nordbayern)**.  
The focus lies on identifying **regional patterns** and **urban–rural differences**
rather than proposing direct political solutions.

The project is designed as an **exploratory data analysis** that aims to make
structural disparities visible and encourage further discussion.

---

## 🎯 Project Objective

The objective of this project is to:

- compare unemployment rates of **women and men**
- analyze the **gender gap** in unemployment
- focus on **regional differences within North Bavaria**
- highlight contrasts between **urban and rural regions**

This analysis does **not** aim to solve the problem, but rather to **illustrate and
contextualize existing inequalities**.

---

## ⚖️ Analysis Dimensions

- **Women**  
  Analysis of the female unemployment rate across selected regions in North Bavaria.

- **Men**  
  Analysis of the male unemployment rate across the same regions.

- **Gender Gap**  
  Difference between female and male unemployment rates
  (female rate minus male rate).

---

## 🚀 Features

- Automated data loading and cleaning using **pandas**
- Regional filtering with focus on **North Bavaria**
- Gender-based comparison of unemployment rates
- Calculation and visualization of the **gender gap**
- Clear and reproducible visualizations using **Matplotlib**

---

## 📁 Project Structure

### 📂 Outputs/
- **01_frauen_vs_maenner.png**  
  Comparison of unemployment rates between women and men by region  
  *(selection: North Bavaria)*

- **02_gender_gap.png**  
  Visualization of the gender gap in unemployment rates by region

- **03_gesamt.png**  
  Overall unemployment rate per region

---

### 📂 src/
- **config.py**  
  Configuration file (file paths, column names, CSV settings)

- **data_loader.py**  
  Loading, cleaning, and preprocessing of the CSV data

- **plots.py**  
  Generation of bar charts and comparative visualizations

- **utils.py**  
  Helper functions (e.g. directory creation)

---

## 📊 Interpretation of Results

The generated visualizations highlight that:

- unemployment rates differ noticeably across regions
- gender-specific differences vary depending on regional context
- urban and rural labor markets show distinct patterns

The results should be interpreted as **descriptive insights** rather than causal explanations.

---

## 🛠 Installation & Usage
This project can be executed locally to reproduce the analysis and vizualisations.

### 1. Install dependencies:
Install all the required Python packages using:

```bash
pip install -r requirements.txt

```
### 2. Run the analysis:
Execute the main script to load the data, process it, and generate the visualizations:

```bash
python main.py

```
The generated figures will be saved automatically in the Outputs/folder.

---

## ℹ️ Notes on Data

The CSV file path and column names are defined in config.py.
The analysis is fully reproducible based on the provided configuration and input data.

## 📌 Disclaimer

This project serves academic and illustrative purposes.
It does not claim completeness or policy relevance, but aims to support
data-driven discussion on regional labor market inequalities.
