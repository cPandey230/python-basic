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

    # Addition with fill_value
    add_result = df1.add(df2, fill_value=0)
    print("\nAddition with fill_value=0:")
    print(add_result)

    # Subtraction with fill_value
    sub_result = df1.sub(df2, fill_value=0)
    print("\nSubtraction with fill_value=0:")
    print(sub_result)

    # Division with fill_value
    div_result = df1.div(df2, fill_value=1)
    print("\nDivision with fill_value=1:")
    print(div_result)

    # Floor Division with fill_value
    floordiv_result = df1.floordiv(df2, fill_value=1)
    print("\nFloor Division with fill_value=1:")
    print(floordiv_result)

    # Multiplication with fill_value
    mul_result = df1.mul(df2, fill_value=1)
    print("\nMultiplication with fill_value=1:")
    print(mul_result)

    # Exponentiation with fill_value
    pow_result = df1.pow(df2, fill_value=1)
    print("\nExponentiation with fill_value=1:")
    print(pow_result)


if __name__ == "__main__":
    main()
