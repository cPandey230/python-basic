import numpy as np


def main():
    # Create a sample array
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # Sum of all elements
    sum_all = np.sum(arr)
    print("Sum of all elements:", sum_all)

    # Sum along axis 0 (columns)
    sum_axis0 = np.sum(arr, axis=0)
    print("Sum along axis 0 (columns):", sum_axis0)

    # Sum along axis 1 (rows)
    sum_axis1 = np.sum(arr, axis=1)
    print("Sum along axis 1 (rows):", sum_axis1)

    # # Mean of all elements
    # mean_all = np.mean(arr)
    # print("Mean of all elements:", mean_all)

    # # Standard deviation
    # std_all = np.std(arr)
    # print("Standard deviation of all elements:", std_all)

    # # Variance
    # var_all = np.var(arr)
    # print("Variance of all elements:", var_all)

    # # Minimum value
    # min_val = np.min(arr)
    # print("Minimum value:", min_val)

    # # Maximum value
    # max_val = np.max(arr)
    # print("Maximum value:", max_val)

    # # Index of minimum value
    # argmin_val = np.argmin(arr)
    # print("Index of minimum value:", argmin_val)

    # # Index of maximum value
    # argmax_val = np.argmax(arr)
    # print("Index of maximum value:", argmax_val)

    # # Cumulative sum
    # cumsum_val = np.cumsum(arr)
    # print("Cumulative sum of elements:", cumsum_val)

    # # Cumulative product
    # cumprod_val = np.cumprod(arr)
    # print("Cumulative product of elements:", cumprod_val)


if __name__ == "__main__":
    main()
