import pandas as pd
import numpy as np


def main():
    data = pd.DataFrame(
        np.arange(12).reshape((3, 4)),
        index=["Ohio", "Colorado", "New York"],
        columns=["one", "two", "three", "four"],
    )

    print("Original DataFrame:")
    print(data)

    # Transform function to convert first 4 letters to uppercase
    transform = lambda x: x[:4].upper()

    # Applying the transform function to the index
    data.index = data.index.map(transform)
    print("\nDataFrame with transformed index labels:")
    print(data)

    # Renaming index and columns using functions
    data_renamed = data.rename(index=str.title, columns=str.upper)
    print("\nDataFrame with renamed index and columns using functions:")
    print(data_renamed)

    # Renaming specific index and columns using dictionary-like objects
    data_renamed_dict = data.rename(
        index={"OHIO": "INDIANA"}, columns={"three": "peekaboo"}
    )
    print("\nDataFrame with specific index and columns renamed using dictionaries:")
    print(data_renamed_dict)

    # Renaming index in-place
    data.rename(index={"OHIO": "INDIANA"}, inplace=True)
    print("\nDataFrame with index renamed in-place:")
    print(data)


if __name__ == "__main__":
    main()
