import pandas as pd


def main():
    # Creating a DataFrame
    data = {"A": [1, 2, 3, 4, 5], "B": [5, 4, 3, 2, 1]}
    df = pd.DataFrame(data)

    # Creating Index objects
    index1 = pd.Index([1, 2, 3, 4, 5])
    index2 = pd.Index([3, 4, 5, 6, 7])

    # Append: Concatenate with additional Index objects, producing a new Index
    appended_index = index1.append(index2)
    print("Appended Index:", appended_index)

    # Difference: Compute set difference as an Index
    difference_index = index1.difference(index2)
    print("Difference Index:", difference_index)

    # Intersection: Compute set intersection
    intersection_index = index1.intersection(index2)
    print("Intersection Index:", intersection_index)

    # Union: Compute set union
    union_index = index1.union(index2)
    print("Union Index:", union_index)

    # Isin: Compute boolean array indicating whether each value is contained in the passed collection
    isin_array = index1.isin(index2)
    print("Isin array:", isin_array)

    # Delete: Compute new Index with element at index i deleted
    deleted_index = index1.delete(2)
    print("Deleted Index:", deleted_index)

    # Drop: Compute new Index by deleting passed values
    dropped_index = index1.drop([2, 3])
    print("Dropped Index:", dropped_index)

    # Insert: Compute new Index by inserting element at index i
    inserted_index = index1.insert(2, 10)
    print("Inserted Index:", inserted_index)

    # Is_monotonic: Returns True if each element is greater than or equal to the previous element
    is_monotonic = index1.is_monotonic
    print("Is monotonic:", is_monotonic)

    # Is_unique: Returns True if the Index has no duplicate values
    is_unique = index1.is_unique
    print("Is unique:", is_unique)

    # Unique: Compute the array of unique values in the Index
    unique_values = index1.unique()
    print("Unique values:", unique_values)

    # Using Index methods with DataFrame
    # Setting an index for the DataFrame
    df.set_index("A", inplace=True)
    print("\nDataFrame with index set to column 'A':")
    print(df)

    # Using the same methods on DataFrame index
    appended_index_df = df.index.append(pd.Index([6, 7]))
    print("Appended Index to DataFrame index:", appended_index_df)

    difference_index_df = df.index.difference(pd.Index([2, 3]))
    print("Difference Index in DataFrame index:", difference_index_df)

    intersection_index_df = df.index.intersection(pd.Index([1, 2, 3]))
    print("Intersection Index in DataFrame index:", intersection_index_df)

    union_index_df = df.index.union(pd.Index([6, 7]))
    print("Union Index in DataFrame index:", union_index_df)

    isin_array_df = df.index.isin([2, 3, 4])
    print("Isin array in DataFrame index:", isin_array_df)

    deleted_index_df = df.index.delete(1)
    print("Deleted Index in DataFrame index:", deleted_index_df)

    dropped_index_df = df.index.drop([2, 3])
    print("Dropped Index in DataFrame index:", dropped_index_df)

    inserted_index_df = df.index.insert(1, 10)
    print("Inserted Index in DataFrame index:", inserted_index_df)

    is_monotonic_df = df.index.is_monotonic
    print("Is monotonic in DataFrame index:", is_monotonic_df)

    is_unique_df = df.index.is_unique
    print("Is unique in DataFrame index:", is_unique_df)

    unique_values_df = df.index.unique()
    print("Unique values in DataFrame index:", unique_values_df)


if __name__ == "__main__":
    main()
