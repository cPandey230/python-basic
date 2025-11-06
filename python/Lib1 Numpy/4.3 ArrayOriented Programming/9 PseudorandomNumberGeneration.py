import numpy as np


def main():
    # Seed the random number generator
    np.random.seed(42)

    # permutation(): Return a random permutation of a sequence, or return a permuted range
    perm = np.random.permutation(10)
    print("Random permutation of range 10:", perm)  # Output: [2 8 4 9 1 6 7 3 0 5]

    # shuffle(): Randomly permute a sequence in-place
    arr = np.arange(10)
    np.random.shuffle(arr)
    print("Shuffled array:", arr)

    # rand(): Draw samples from a uniform distribution
    uniform_samples = np.random.rand(5)
    print("Uniform distribution samples:", uniform_samples)

    # randint(): Draw random integers from a given low-to-high range
    random_integers = np.random.randint(1, 10, size=5)
    print("Random integers:", random_integers)

    # randn(): Draw samples from a normal distribution with mean 0 and standard deviation 1 (MATLAB-like interface)
    normal_samples = np.random.randn(5)
    print("Normal distribution samples:", normal_samples)

    # binomial(): Draw samples from a binomial distribution
    binomial_samples = np.random.binomial(n=10, p=0.5, size=5)
    print("Binomial distribution samples:", binomial_samples)

    # normal(): Draw samples from a normal (Gaussian) distribution
    normal_gaussian_samples = np.random.normal(loc=0, scale=1, size=5)
    print("Gaussian distribution samples:", normal_gaussian_samples)

    # beta(): Draw samples from a beta distribution
    beta_samples = np.random.beta(a=2, b=5, size=5)
    print("Beta distribution samples:", beta_samples)

    # chisquare(): Draw samples from a chi-square distribution
    chisquare_samples = np.random.chisquare(df=2, size=5)
    print("Chi-square distribution samples:", chisquare_samples)

    # gamma(): Draw samples from a gamma distribution
    gamma_samples = np.random.gamma(shape=2, scale=1, size=5)
    print("Gamma distribution samples:", gamma_samples)

    # uniform(): Draw samples from a uniform [0, 1) distribution
    uniform_01_samples = np.random.uniform(low=0.0, high=1.0, size=5)
    print("Uniform [0, 1) distribution samples:", uniform_01_samples)


if __name__ == "__main__":
    main()
