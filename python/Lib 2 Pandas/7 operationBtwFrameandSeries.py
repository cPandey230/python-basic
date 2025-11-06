import pandas as pd
import numpy as np


def main():
    # Creating a 2D array and performing broadcasting
    arr = np.arange(12.0).reshape((3, 4))
    print("2D array:")
    print(arr)

    # Subtracting a row from the 2D array
    print("\nSubtracting arr[0] from arr:")
    print(arr - arr[0])

    # Creating a DataFrame
    frame = pd.DataFrame(
        np.arange(12.0).reshape((4, 3)),
        columns=list("bde"),
        index=["Utah", "Ohio", "Texas", "Oregon"],
    )
    print("\nDataFrame:")
    print(frame)

    # Creating a Series
    series = frame.iloc[0]
    print("\nSeries:")
    print(series)

    # Arithmetic between DataFrame and Series (broadcasting)
    print("\nDataFrame - Series:")
    print(frame - series)

    # Reindexing example
    series2 = pd.Series(range(3), index=["b", "e", "f"])
    print("\nSeries2 (for reindexing):")
    print(series2)

    print("\nDataFrame + Series2 (reindexing):")
    print(frame + series2)

    # Broadcasting over columns
    series3 = frame["d"]
    print("\nSeries3 (for broadcasting over columns):")
    print(series3)

    print("\nDataFrame - Series3 (broadcasting over columns):")
    print(frame.sub(series3, axis="index"))


if __name__ == "__main__":
    main()
