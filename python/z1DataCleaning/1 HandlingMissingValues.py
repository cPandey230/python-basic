import pandas as pd
import numpy as np


def main():
    df = pd.DataFrame(
        {
            "A": [1, 2, np.nan, 4],
            "B": [5, np.nan, np.nan, 8],
            "C": [np.nan, 10, 11, 12],
        }
    )

    print(f"Dataframe : \n{df}")

    dfdropna = df.dropna()
    print(f"Datframe after using 'dropna' : \n {dfdropna}")

    dffillna = df.fillna(0)
    print(f"Datframe after using 'fillna' : \n {dffillna}")

    dfisNull = df.isnull()
    print(f"Datframe after using 'isnull' : \n {dfisNull}")

    dfnotNull = df.notnull()
    print(f"Datframe after using 'isnull' : \n {dfnotNull}")


if __name__ == "__main__":
    main()
