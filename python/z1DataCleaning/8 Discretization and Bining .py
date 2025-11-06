import pandas as pd
import numpy as np


def main():
    # Sample ages data
    ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]

    # Bins for age groups
    bins = [18, 25, 35, 60, 100]

    # Perform binning using cut
    cats = pd.cut(ages, bins)
    print("Categorical data with bins:")
    print(cats)

    # Display bin codes
    print("\nBin codes:")
    print(cats.codes)

    # Display bin categories
    print("\nBin categories:")
    print(cats.categories)

    # Count values in each bin
    print("\nValue counts for each bin:")
    print(pd.value_counts(cats))

    # Changing the closed side of intervals to left (right=False)
    cats_left = pd.cut(ages, [18, 26, 36, 61, 100], right=False)
    print("\nBinning with left-closed intervals:")
    print(cats_left)

    # Custom labels for bins
    group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]

    # Applying custom labels
    labeled_cats = pd.cut(ages, bins, labels=group_names)
    print("\nBinning with custom labels:")
    print(labeled_cats)

    # Creating uniformly distributed data
    data = np.random.rand(20)

    # Binning into 4 equal-length bins
    equal_bins = pd.cut(data, 4, precision=2)
    print("\nEqual-length binning:")
    print(equal_bins)

    # Normally distributed data
    data = np.random.randn(1000)

    # Quantile-based binning into quartiles
    quartile_bins = pd.qcut(data, 4)
    print("\nQuantile-based binning:")
    print(quartile_bins)

    # Count values in each quantile bin
    print("\nValue counts for each quantile bin:")
    print(pd.value_counts(quartile_bins))

    # Custom quantiles
    custom_quantiles = pd.qcut(data, [0, 0.1, 0.5, 0.9, 1.0])
    print("\nCustom quantile-based binning:")
    print(custom_quantiles)


if __name__ == "__main__":
    main()
