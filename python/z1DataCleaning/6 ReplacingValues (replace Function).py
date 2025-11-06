# DataFrame.replace(
#     to_replace=None, value=None, inplace=False, limit=None, regex=False, method="pad"
# )

import pandas as pd
import numpy as np


def main():
    df = pd.DataFrame(
        {
            "A": [1, 2, np.nan, 4],
            "B": [np.nan, 2, 3, np.nan],
            "C": [1, np.nan, np.nan, 4],
            "D": [np.nan, np.nan, np.nan, np.nan],
        }
    )

    print("Original DataFrame:")
    print(df)

    # Replace NaN with 0
    df_replace_nan = df.replace(np.nan, 0)
    print("\nReplace NaN with 0:")
    print(df_replace_nan)

    # Replace NaN with 0 and 4 with 5
    df_replace_multiple = df.replace({np.nan: 0, 4: 5})
    print("\nReplace NaN with 0 and 4 with 5:")
    print(df_replace_multiple)

    # Replace NaN with 0 using lists
    df_replace_list = df.replace([np.nan], [0])
    print("\nReplace NaN with 0 using lists:")
    print(df_replace_list)

    # Replace NaN with 0 in column 'A'
    df_replace_dict = df.replace({"A": {np.nan: 0}})
    print("\nReplace NaN with 0 in column 'A':")
    print(df_replace_dict)

    # Replace all digits with '-' (example for string replacement)
    data_with_strings = {
        "A": ["1", "2", "nan", "4"],
        "B": ["nan", "2", "3", "nan"],
        "C": ["1", "nan", "nan", "4"],
        "D": ["nan", "nan", "nan", "nan"],
    }

    df_strings = pd.DataFrame(data_with_strings)
    df_replace_regex = df_strings.replace(to_replace=r"\d", value="-", regex=True)
    print("\nReplace all digits with '-':")
    print(df_replace_regex)


if __name__ == "__main__":
    main()
