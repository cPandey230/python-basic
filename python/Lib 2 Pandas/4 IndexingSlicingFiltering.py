import pandas as pd


def main():
    # Creating a sample DataFrame
    data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1], "C": [2, 3, 4, 5, 6]}
    df = pd.DataFrame(data)

    print(f"Original DataFrame:\n{df}\n")

    # df[val]: Select single column
    column_a = df["A"]
    print(f"Select single column 'A':\n{column_a}\n")

    # df[val]: Select sequence of columns
    columns_a_b = df[["A", "B"]]
    print(f"Select columns 'A' and 'B':\n{columns_a_b}\n")

    # df.loc[val]: Select single row by label
    row_2 = df.loc[2]
    print(f"Select row with label 2:\n{row_2}\n")

    # df.loc[:, val]: Select single column by label
    column_b = df.loc[:, "B"]
    print(f"Select column 'B' using loc[:, 'B']:\n{column_b}\n")

    # df.loc[val1, val2]: Select rows and columns by label
    row_2_column_b = df.loc[2, "B"]
    print(f"Select row 2 and column 'B': {row_2_column_b}\n")

    # df.iloc[where]: Select single row by integer position
    row_3 = df.iloc[3]
    print(f"Select row with integer position 3:\n{row_3}\n")

    # df.iloc[:, where]: Select single column by integer position
    column_1 = df.iloc[:, 1]
    print(f"Select column with integer position 1:\n{column_1}\n")

    # df.iloc[where_i, where_j]: Select rows and columns by integer position
    row_3_column_1 = df.iloc[3, 1]
    print(f"Select row 3 and column 1 by integer position: {row_3_column_1}\n")

    # df.at[label_i, label_j]: Select a single scalar value by label
    scalar_value = df.at[2, "C"]
    print(f"Select scalar value at row 2, column 'C': {scalar_value}\n")

    # df.iat[i, j]: Select a single scalar value by integer position
    scalar_value_int = df.iat[2, 2]
    print(
        f"Select scalar value at row 2, column 2 by integer position: {scalar_value_int}\n"
    )

    # Reindex method: Select rows by labels
    new_index = [0, 2, 4]
    reindexed_df = df.reindex(new_index)
    print(f"Reindexed DataFrame (rows 0, 2, 4):\n{reindexed_df}\n")

    # get_value and set_value methods: Select and set single value by label
    old_value = df.at[1, "A"]
    df.at[1, "A"] = 10
    new_value = df.at[1, "A"]
    print(f"Old value at row 1, column 'A': {old_value}\n")
    print(f"New value at row 1, column 'A': {new_value}\n")


if __name__ == "__main__":
    main()
