import pandas as pd
import numpy as np


def main():
    # Creating two DataFrames
    df1 = pd.DataFrame(
        {"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]}, index=["X", "Y", "Z"]
    )
    df2 = pd.DataFrame(
        {"A": [9, 8, 7], "B": [6, 5, 4], "D": [3, 2, 1]}, index=["X", "Y", "W"]
    )

    print("DataFrame 1:")
    print(df1)
    print("\nDataFrame 2:")
    print(df2)

    # Adding DataFrames
    print("\nAddition (df1 + df2):")
    print(df1 + df2)

    # Subtracting DataFrames
    print("\nSubtraction (df1 - df2):")
    print(df1 - df2)

    # Multiplying DataFrames
    print("\nMultiplication (df1 * df2):")
    print(df1 * df2)

    # Dividing DataFrames
    print("\nDivision (df1 / df2):")
    print(df1 / df2)

    # Using fill_value to handle missing data
    print("\nAddition with fill_value=0 (df1.add(df2, fill_value=0)):")
    print(df1.add(df2, fill_value=0))

    # Using arithmetic methods with fill_value
    print("\nSubtraction with fill_value=0 (df1.sub(df2, fill_value=0)):")
    print(df1.sub(df2, fill_value=0))

    print("\nMultiplication with fill_value=1 (df1.mul(df2, fill_value=1)):")
    print(df1.mul(df2, fill_value=1))

    print("\nDivision with fill_value=1 (df1.div(df2, fill_value=1)):")
    print(df1.div(df2, fill_value=1))


if __name__ == "__main__":
    main()
