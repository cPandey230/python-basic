import pandas as pd
import numpy as np


def main():
    # Creating a DataFrame with 5 rows and 4 columns
    df = pd.DataFrame(np.arange(20).reshape((5, 4)))
    print("Original DataFrame:")
    print(df)

    # Generating a random permutation of row indices
    sampler = np.random.permutation(5)
    print("\nRandom permutation of row indices:")
    print(sampler)

    # Using iloc-based indexing with the permutation
    df_permuted = df.take(sampler)
    print("\nDataFrame with permuted rows:")
    print(df_permuted)

    # Selecting a random subset of 3 rows without replacement
    df_sampled = df.sample(n=3)
    print("\nRandom subset of 3 rows (without replacement):")
    print(df_sampled)

    # Creating a Series for demonstration
    choices = pd.Series([5, 7, -1, 6, 4])

    # Generating a sample of 10 elements with replacement
    draws = choices.sample(n=10, replace=True)
    print("\nRandom sample of 10 elements (with replacement):")
    print(draws)


if __name__ == "__main__":
    main()
