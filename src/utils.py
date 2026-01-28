def prepare_gender_pivot(df):
    """
    Prepare pivot table with unemployment rates by year and gender.
    """
    return df.pivot_table(
        index="year",
        columns="gender",
        values="unemployment_rate"
    ).reset_index()


def calculate_gender_gap(df):
    """
    Calculate gender gap (Women - Men).
    """
    pivot = prepare_gender_pivot(df)
    pivot["Gender Gap"] = pivot["Women"] - pivot["Men"]
    return pivot
