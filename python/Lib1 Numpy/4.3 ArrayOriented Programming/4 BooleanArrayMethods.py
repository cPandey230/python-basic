# boolean array methods

import numpy as np


def main():
    arr = np.array([True, False, True])

    # np.any() : Checks if any element in the array is True.
    print(f"{np.any(arr)}")

    # np.all() : Checks if all elements in the array are True.
    print(f"{np.all(arr)}")

    # np.sum() : Counts the number of true elements in array
    print(f"{np.sum(arr)}")

    # np.nonzero() : Return the index of true elments
    print(f"{np.nonzero(arr)}")

    # np.where() : Return indeces where the condition is True
    print(f"{np.where(arr)}")

    # logical operaators
    arr1 = np.array([False, False, True])
    print(f"{np.logical_and(arr,arr1)}")
    print(f"{np.logical_or(arr,arr1)}")
    print(f"{np.logical_not(arr)}")
    print(f"{np.logical_xor(arr,arr1)}")

    # masking and indexing
    data = np.array([1, 2, 3, 4, 5])
    mask = np.array([True, False, True, False, True])
    print(f"{data[mask]}")


if __name__ == "__main__":
    main()
