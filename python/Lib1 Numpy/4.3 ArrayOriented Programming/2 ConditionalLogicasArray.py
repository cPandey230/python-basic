# Expressing Conditional Logic as Array Operations

import numpy as np


def main():
    arr1 = np.array([[1, 2, 3], [4, 5, 6]])
    arr2 = np.array([[6, 5, 4], [3, 2, 1]])

    # # Element-wise Comparison
    # greater_than = arr1 > arr2
    # print(f"arr1 > arr2 \n {greater_than}")

    # # Element-wise Conditional Assignment with np.where
    # result = np.where(arr1 > arr2, arr1, arr2)
    # print(f"Result of np.where : \n {result}")

    # # Applying a Condition to Filter Elements
    # filtered = arr1[arr1 > 3]
    # print(f"Elements in arr1 greater than 3: \n {filtered}")

    # # using Boolean Masks
    # mask = arr1 > 2
    # print(f"Boolean mask:\n {mask}")

    # arr1[mask] = 0
    # print(f"arr1 after aplying mask:\n{arr1}")

    # # Combining Conditions
    # combined_condition = (arr1 > 0) & (arr1 < 3)
    # print(f"Combined condition mask:\n{combined_condition}")


if __name__ == "__main__":
    main()
