import pandas as pd
import numpy as np


def main():
    # Dropping entries from a Series
    obj = pd.Series(np.arange(5.0), index=["a", "b", "c", "d", "e"])
    print(f"Original Series:\n{obj}\n")

    # Dropping a single entry from a Series
    new_obj = obj.drop("c")
    print(f"Series after dropping 'c':\n{new_obj}\n")

    # Dropping multiple entries from a Series
    new_obj_multi = obj.drop(["d", "c"])
    print(f"Series after dropping 'd' and 'c':\n{new_obj_multi}\n")

    # Using inplace=True to modify the Series in place
    obj.drop("c", inplace=True)
    print(f"Series after dropping 'c' with inplace=True:\n{obj}\n")

    # Reset the Series for further demonstration
    obj = pd.Series(np.arange(5.0), index=["a", "b", "c", "d", "e"])

    # Creating a DataFrame
    data = pd.DataFrame(
        np.arange(16).reshape((4, 4)),
        index=["Ohio", "Colorado", "Utah", "New York"],
        columns=["one", "two", "three", "four"],
    )
    print(f"Original DataFrame:\n{data}\n")

    # Dropping rows from a DataFrame
    data_dropped_rows = data.drop(["Colorado", "Ohio"])
    print(
        f"DataFrame after dropping rows 'Colorado' and 'Ohio':\n{data_dropped_rows}\n"
    )

    # Dropping a column from a DataFrame
    data_dropped_column = data.drop("two", axis=1)
    print(f"DataFrame after dropping column 'two':\n{data_dropped_column}\n")

    # Dropping multiple columns from a DataFrame
    data_dropped_columns = data.drop(["two", "four"], axis="columns")
    print(
        f"DataFrame after dropping columns 'two' and 'four':\n{data_dropped_columns}\n"
    )

    # Using inplace=True to modify the DataFrame in place
    data.drop(["two", "four"], axis="columns", inplace=True)
    print(
        f"DataFrame after dropping columns 'two' and 'four' with inplace=True:\n{data}\n"
    )


if __name__ == "__main__":
    main()
