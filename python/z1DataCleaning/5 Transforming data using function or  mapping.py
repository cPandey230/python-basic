import pandas as pd


def main():

    data = pd.DataFrame(
        {
            "food": [
                "bacon",
                "pulled pork",
                "bacon",
                "Pastrami",
                "corned beef",
                "Bacon",
                "pastrami",
                "honey ham",
                "nova lox",
            ],
            "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6],
        }
    )

    print(f"Original Datframe : \n{data}")

    # Mapping of meat to animal
    meat_to_animal = {
        "bacon": "pig",
        "pulled pork": "pig",
        "pastrami": "cow",
        "corned beef": "cow",
        "honey ham": "pig",
        "nova lox": "salmon",
    }

    # Convert food column to lowercase
    lowercased = data["food"].str.lower()

    # map the lowercase food items to their respective animals
    data["animal"] = lowercased.map(meat_to_animal)
    print(f"\nDataFrame after mapping 'food' to 'animal': \n{data}")

    # Alternatively, using a lambda function
    data["animal"] = data["food"].map(lambda x: meat_to_animal[x.lower()])

    print("\nDataFrame using lambda function to map 'food' to 'animal':")
    print(data)


if __name__ == "__main__":
    main()
