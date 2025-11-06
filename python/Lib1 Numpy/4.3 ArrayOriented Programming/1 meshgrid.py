import numpy as np


def main():
    # points = np.arange(-5, 5, 0.01)
    points1 = np.random.randint(1, 100, size=9)
    points2 = np.random.randint(1, 100, size=9)

    # xs, xy = np.meshgrid(points, points)
    xs, xy = np.meshgrid(points1, points2)
    print(f"Shape of xs(for rows) is {xs.shape}")
    print(f"Shape of xy(for columns) is {xy.shape}")
    print(f"Shape of points1 is {points1.shape}")
    print(f"Shape of points2 is {points2.shape}")

    print(f"{xs}")
    print()
    print(f"{xy}")


if __name__ == "__main__":
    main()
