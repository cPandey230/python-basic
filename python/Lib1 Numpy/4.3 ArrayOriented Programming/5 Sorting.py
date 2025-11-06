import numpy as np


def main():
    arr = [5, 3, 1, 4, 2]

    # Convert the list to a NumPy array
    arr_np = np.array(arr)

    # np.sort(): Returns a sorted copy of the array.
    sorted_arr = np.sort(arr_np)
    print("Sorted array:", sorted_arr)  # Output: [1 2 3 4 5]

    # ndarray.sort(): Sorts the array in place.
    arr_np.sort()
    print("Array sorted in place:", arr_np)  # Output: [1 2 3 4 5]

    # np.argsort() : Returns the indices that would sort the array.
    sorted_indices = np.argsort(arr_np)
    print("Indices of sorted array:", sorted_indices)  # Output: [0 1 2 3 4]

    # Use the indices to get the sorted array
    sorted_arr_using_indices = arr_np[sorted_indices]
    print(
        "Sorted array using indices:", sorted_arr_using_indices
    )  # Output: [1 2 3 4 5]

    # Sorting Multidimensional arrays
    # np.sort() and ndarray.sort() can be used to sort along a specific axis.

    arr2d = np.array([[5, 3, 1], [4, 2, 6]])
    print("Original 2D array:\n", arr2d)

    sorted_arr_axis0 = np.sort(arr2d, axis=0)
    print("Array sorted along axis 0 (columns):\n", sorted_arr_axis0)

    sorted_arr_axis1 = np.sort(arr2d, axis=1)
    print("Array sorted along axis 1 (rows):\n", sorted_arr_axis1)


if __name__ == "__main__":
    main()
