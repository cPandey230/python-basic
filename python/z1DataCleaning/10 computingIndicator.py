import pandas as pd
import numpy as np


def main():
    # Creating a simple DataFrame
    df = pd.DataFrame({"key": ["b", "b", "a", "c", "a", "b"], "data1": range(6)})
    print("Original DataFrame:")
    print(df)

    # Creating dummy variables
    dummies = pd.get_dummies(df["key"])
    print("\nDummy Variables:")
    print(dummies)

    # Adding prefix to dummy variable columns
    dummies_prefixed = pd.get_dummies(df["key"], prefix="key")
    df_with_dummy = df[["data1"]].join(dummies_prefixed)
    print("\nDataFrame with Dummy Variables:")
    print(df_with_dummy)

    # Example with multiple categories
    movies = pd.DataFrame(
        {
            "movie_id": [1, 2, 3],
            "title": ["Toy Story (1995)", "Jumanji (1995)", "Grumpier Old Men (1995)"],
            "genres": [
                "Animation|Children's|Comedy",
                "Adventure|Children's|Fantasy",
                "Comedy|Romance",
            ],
        }
    )
    print("\nMovies DataFrame:")
    print(movies)

    # Extracting unique genres
    all_genres = []
    for x in movies["genres"]:
        all_genres.extend(x.split("|"))
    genres = pd.unique(all_genres)
    print("\nUnique Genres:")
    print(genres)

    # Creating indicator DataFrame
    zero_matrix = np.zeros((len(movies), len(genres)))
    dummies = pd.DataFrame(zero_matrix, columns=genres)
    for i, gen in enumerate(movies["genres"]):
        indices = dummies.columns.get_indexer(gen.split("|"))
        dummies.iloc[i, indices] = 1
    movies_windic = movies.join(dummies.add_prefix("Genre_"))
    print("\nMovies DataFrame with Indicator Variables:")
    print(movies_windic)

    # Discretization with dummy variables
    np.random.seed(12345)
    values = np.random.rand(10)
    print("\nRandom Values:")
    print(values)
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    cut_values = pd.cut(values, bins)
    print("\nBinned Values:")
    print(cut_values)
    dummies_cut = pd.get_dummies(cut_values)
    print("\nDummy Variables for Binned Values:")
    print(dummies_cut)


if __name__ == "__main__":
    main()
