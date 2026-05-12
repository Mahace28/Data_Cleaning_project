def clean_dataset(df):

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing math scores with average
    df["math score"] = df["math score"].fillna(
        df["math score"].mean()
    )

    # Fill missing reading scores
    df["reading score"] = df["reading score"].fillna(
        df["reading score"].mean()
    )

    # Fill missing writing scores
    df["writing score"] = df["writing score"].fillna(
        df["writing score"].mean()
    )

    return df