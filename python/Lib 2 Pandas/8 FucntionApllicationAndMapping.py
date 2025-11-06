import pandas as pd
import numpy as np


def main():
    # Create a DataFrame with random values
    frame = pd.DataFrame(
        np.random.randn(4, 3),
        columns=list("bde"),
        index=["Utah", "Ohio", "Texas", "Oregon"],
    )
    print("Original DataFrame:")
    print(frame)

    # Using NumPy ufunc (np.abs) on the DataFrame
    abs_frame = np.abs(frame)
    print("\nDataFrame with np.abs applied:")
    print(abs_frame)

    # Apply a function to each column
    f = lambda x: x.max() - x.min()
    column_diff = frame.apply(f)
    print("\nDifference between max and min for each column:")
    print(column_diff)

    # Apply a function to each row
    row_diff = frame.apply(f, axis="columns")
    print("\nDifference between max and min for each row:")
    print(row_diff)

    # Apply a function that returns a Series
    def min_max(x):
        return pd.Series([x.min(), x.max()], index=["min", "max"])

    min_max_frame = frame.apply(min_max)
    print("\nMin and Max values for each column:")
    print(min_max_frame)

    # Apply element-wise function with applymap
    format_func = lambda x: "%.2f" % x
    formatted_frame = frame.applymap(format_func)
    print("\nFormatted DataFrame (each value as string with 2 decimal places):")
    print(formatted_frame)

    # Apply element-wise function with map on a Series
    formatted_series = frame["e"].map(format_func)
    print("\nFormatted Series (column 'e'):")
    print(formatted_series)


if __name__ == "__main__":
    main()
