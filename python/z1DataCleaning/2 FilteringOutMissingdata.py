import pandas as pd
import numpy as np
from numpy import nan as NA


def main():
    data = pd.DataFrame(
        [
            [1, 2, 3, 4],
            [1.0, 6.5, 3.0, NA],
            [1.0, NA, NA, NA],
            [NA, NA, NA, NA],
            [NA, 6.5, 3.0, NA],
        ]
    )
    print(f"Oringinal Dataframe : \n {data}")
    cleaned_df = data.dropna()

    # Drop rows where all values are NaN
    dropRows = data.dropna(how="all")
    print(f"Droping rows where all values are NaN : \n{dropRows}")

    # Drop columns where all values are NaN
    dropColumns = data.dropna(axis=1, how="all")
    print(f"Drop columns where all values are NaN :\n{dropColumns}")

    # Using thresh to specify minimum non-null values
    threshData = data.dropna(thresh=2)
    print(f"By using thresh removing 2 nan from each column: \n{threshData}")


if __name__ == "__main__":
    main()
