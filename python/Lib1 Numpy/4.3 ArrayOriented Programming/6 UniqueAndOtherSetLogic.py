import numpy as np


def main():
    x = np.array([1, 2, 3, 4, 5, 5, 6])
    y = np.array([4, 5, 6, 7, 8])

    # unique(): Compute the sorted, unique elements in x
    unique_x = np.unique(x)
    print(f"Unique elements in x : {unique_x}")

    # intersect1d(): Compute the sorted, common elements in x and y
    common_elements = np.intersect1d(x, y)
    print(f"Common elments in x and y : {common_elements}")

    # union1d() : Compute the sorted union of elments
    union_elements = np.union1d(x, y)
    print(f"Union of elments in x and y : {union_elements}")

    # in1d(): Compute a boolean array indicating whether each element of x is contained in y
    is_in_y = np.in1d(x, y)
    print(f"Elements of x contained in y : {is_in_y}")

    # setdiff1d(): Set difference, elements in x that are not in y
    diff_elements = np.setdiff1d(x, y)
    print(f"Elements in x that are not in y : {diff_elements}")

    # setxor1d(): Set symmetric differences; elements that are in either of the arrays, but not both
    xor_elements = np.setxor1d(x, y)
    print(f"Symmetric differences between x and y : {xor_elements}")


if __name__ == "__main__":
    main()
