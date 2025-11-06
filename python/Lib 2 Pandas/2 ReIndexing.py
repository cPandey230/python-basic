import pandas as pd


def main():
    # Creating a sample DataFrame
    data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data, index=[0, 1, 2, 3, 4])

    print(f"Original DataFrame:\n{df}\n")

    # New index sequence
    new_index = [0, 2, 4, 6]

    # Reindexing with new sequence
    reindexed_df = df.reindex(new_index)
    print(f"Reindexed DataFrame:\n{reindexed_df}\n")

    # Using method parameter (forward fill)
    reindexed_ffill_df = df.reindex(new_index, method="ffill")
    print(f"Reindexed DataFrame with forward fill:\n{reindexed_ffill_df}\n")

    # Using fill_value parameter
    reindexed_fill_value_df = df.reindex(new_index, fill_value=0)
    print(f"Reindexed DataFrame with fill_value=0:\n{reindexed_fill_value_df}\n")

    # Using limit parameter with forward fill
    reindexed_limit_df = df.reindex(new_index, method="ffill", limit=1)
    print(f"Reindexed DataFrame with forward fill and limit=1:\n{reindexed_limit_df}\n")

    # Using tolerance parameter
    tolerance_index = [0, 1.5, 2.5, 4]
    reindexed_tolerance_df = df.reindex(
        tolerance_index, method="nearest", tolerance=0.5
    )
    print(f"Reindexed DataFrame with tolerance=0.5:\n{reindexed_tolerance_df}\n")

    # Reindexing with level (for MultiIndex)
    tuples = [("a", 1), ("a", 2), ("b", 1), ("b", 2)]
    multi_index_df = pd.DataFrame(
        {"A": [1, 2, 3, 4]}, index=pd.MultiIndex.from_tuples(tuples)
    )
    print(f"Original MultiIndex DataFrame:\n{multi_index_df}\n")

    new_multi_index = [("a", 1), ("a", 2), ("b", 1), ("b", 3)]
    reindexed_level_df = multi_index_df.reindex(new_multi_index, level=1)
    print(f"Reindexed MultiIndex DataFrame with level=1:\n{reindexed_level_df}\n")

    # Using copy parameter
    reindexed_copy_df = df.reindex(new_index, copy=True)
    print(f"Reindexed DataFrame with copy=True:\n{reindexed_copy_df}\n")


if __name__ == "__main__":
    main()
