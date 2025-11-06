import pandas as pd


def main():
    df = pd.DataFrame(
        {
            "A": [1, 2, 2, 4, 5, 5, 6, 1],
            "B": [1, 2, 2, 3, 4, 4, 5, 1],
            "C": [1, 2, 3, 4, 5, 6, 7, 1],
            "D": [1, 2, 2, 4, 5, 5, 6, 1],
        }
    )
    print(f"Original Datframe : \n{df}")

    # Identifying duplicate rows
    duplicates = df.duplicated()
    print(f"Boolean Series indicating duplicate rows:\n{duplicates}\n")

    # Remove duplicates rows
    df_no_duplicates = df.drop_duplicates()
    print(f"Dataframe with duplicate rows removed:\n{df_no_duplicates}\n")

    # Remove duplicate rows based on a specific column
    df_no_duplicates_col = df.drop_duplicates(subset=["A"])
    print(
        f"Dataframe with duplicate rows based on column 'A' removed:\n{df_no_duplicates_col}\n"
    )

    # Keep the last occurrence of duplicates
    df_keep_last = df.drop_duplicates(keep="last")
    print(f"Dataframe keeping the last occurrence of duplicate rows:\n{df_keep_last}\n")

    # Remove duplicates in place
    df.drop_duplicates(inplace=True)
    print(f"Original dataframe after removing duplicates inplace:\n{df}")


if __name__ == "__main__":
    main()
