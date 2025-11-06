import pandas as pd
import numpy as np


def main():
    # Sorting by index
    obj = pd.Series(range(4), index=["d", "a", "b", "c"])
    print("Original Series:")
    print(obj)
    sorted_obj = obj.sort_index()
    print("\nSeries sorted by index:")
    print(sorted_obj)

    # DataFrame sorting by index
    frame = pd.DataFrame(
        np.arange(8).reshape((2, 4)),
        index=["three", "one"],
        columns=["d", "a", "b", "c"],
    )
    print("\nOriginal DataFrame:")
    print(frame)
    sorted_frame_index = frame.sort_index()
    print("\nDataFrame sorted by index:")
    print(sorted_frame_index)

    sorted_frame_columns = frame.sort_index(axis=1)
    print("\nDataFrame sorted by columns:")
    print(sorted_frame_columns)

    sorted_frame_columns_desc = frame.sort_index(axis=1, ascending=False)
    print("\nDataFrame sorted by columns in descending order:")
    print(sorted_frame_columns_desc)

    # Sorting by values
    obj_values = pd.Series([4, 7, -3, 2])
    print("\nOriginal Series (for value sorting):")
    print(obj_values)
    sorted_obj_values = obj_values.sort_values()
    print("\nSeries sorted by values:")
    print(sorted_obj_values)

    obj_values_with_nan = pd.Series([4, np.nan, 7, np.nan, -3, 2])
    print("\nOriginal Series (with NaNs):")
    print(obj_values_with_nan)
    sorted_obj_values_with_nan = obj_values_with_nan.sort_values()
    print("\nSeries sorted by values (with NaNs):")
    print(sorted_obj_values_with_nan)

    # Sorting DataFrame by values in one or more columns
    frame_sort_values = pd.DataFrame({"b": [4, 7, -3, 2], "a": [0, 1, 0, 1]})
    print("\nOriginal DataFrame (for value sorting):")
    print(frame_sort_values)
    sorted_frame_by_b = frame_sort_values.sort_values(by="b")
    print("\nDataFrame sorted by column 'b':")
    print(sorted_frame_by_b)

    sorted_frame_by_a_b = frame_sort_values.sort_values(by=["a", "b"])
    print("\nDataFrame sorted by columns 'a' and 'b':")
    print(sorted_frame_by_a_b)

    # Ranking
    obj_rank = pd.Series([7, -5, 7, 4, 2, 0, 4])
    print("\nOriginal Series (for ranking):")
    print(obj_rank)
    ranked_obj = obj_rank.rank()
    print("\nSeries ranked (default):")
    print(ranked_obj)

    ranked_obj_first = obj_rank.rank(method="first")
    print("\nSeries ranked (method='first'):")
    print(ranked_obj_first)

    ranked_obj_desc_max = obj_rank.rank(ascending=False, method="max")
    print("\nSeries ranked (descending, method='max'):")
    print(ranked_obj_desc_max)

    # DataFrame ranking
    frame_rank = pd.DataFrame(
        {"b": [4.3, 7, -3, 2], "a": [0, 1, 0, 1], "c": [-2, 5, 8, -2.5]}
    )
    print("\nOriginal DataFrame (for ranking):")
    print(frame_rank)
    ranked_frame = frame_rank.rank(axis="columns")
    print("\nDataFrame ranked by columns:")
    print(ranked_frame)
    obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
    print("Original Series:")
    print(obj)

    # Default method: 'average'
    ranked_average = obj.rank(method="average")
    print("\nRanking with method='average':")
    print(ranked_average)

    # Method: 'min'
    ranked_min = obj.rank(method="min")
    print("\nRanking with method='min':")
    print(ranked_min)

    # Method: 'max'
    ranked_max = obj.rank(method="max")
    print("\nRanking with method='max':")
    print(ranked_max)

    # Method: 'first'
    ranked_first = obj.rank(method="first")
    print("\nRanking with method='first':")
    print(ranked_first)

    # Method: 'dense'
    ranked_dense = obj.rank(method="dense")
    print("\nRanking with method='dense':")
    print(ranked_dense)


if __name__ == "__main__":
    main()
