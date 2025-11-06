import pandas as pd
import numpy as np


def main():
    data = {
        "A": [1, 2, np.nan, 4],
        "B": [np.nan, 2, 3, np.nan],
        "C": [1, np.nan, np.nan, 4],
        "D": [np.nan, np.nan, np.nan, np.nan],
    }

    df = pd.DataFrame(data)

    print(f"Original dataframe : \n {df}")

    # Fill NaN with a scalar value
    df_fill_value = df.fillna(value=0)
    print(f"\nFill NaN with scalar value 0 : \n{df_fill_value}")

    # Fill NaN using backward fill method along columns
    df_ffill = df.fillna(method="ffill")
    print(f"\nFill NaN using forward fill (ffill) method:\n{df_ffill}")

    # Fill NaN using backward fill method along columns
    df_bfill_axis1 = df.fillna(method="bfill", axis=1)
    print(
        f"\nFill NaN using backward fill (bfill) method along columns (axis=1):\n {df_bfill_axis1}"
    )
    # Fill NaN using forward fill method with limit
    df_ffill_limit = df.fillna(method="ffill", limit=1)
    print("\nFill NaN using forward fill (ffill) method with limit=1:")
    print(df_ffill_limit)

    # Fill NaN with a dictionary value for each column
    df_fill_dict = df.fillna(value={"A": 10, "B": 20, "C": 30, "D": 40})
    print("\nFill NaN with different values for each column:")
    print(df_fill_dict)

    # Fill NaN inplace
    df.fillna(value=0, inplace=True)
    print("\nFill NaN inplace with scalar value 0:")
    print(df)


if __name__ == "__main__":
    main()
