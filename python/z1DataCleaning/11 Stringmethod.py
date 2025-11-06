# # Sample string and list of strings for demonstration
# s = "  Hello World  "
# delimiter = ", "
# words = ["hello", "world"]
# substring = "world"

# # count: Return the number of non-overlapping occurrences of substring in the string
# count = s.count("l")
# print(f"count: {count}")  # Output: 3

# # endswith: Returns True if string ends with suffix
# ends_with = s.endswith("World  ")
# print(f"endswith: {ends_with}")  # Output: True

# # startswith: Returns True if string starts with prefix
# starts_with = s.startswith("  Hello")
# print(f"startswith: {starts_with}")  # Output: True

# # join: Use string as delimiter for concatenating a sequence of other strings
# joined_string = delimiter.join(words)
# print(f"join: {joined_string}")  # Output: "hello, world"

# # index: Return position of first character in substring if found in the string; raises ValueError if not found
# try:
#     position = s.index(substring)
#     print(f"index: {position}")  # Output: 8
# except ValueError:
#     print("index: Substring not found")

# # find: Return position of first character of first occurrence of substring in the string; returns -1 if not found
# find_position = s.find(substring)
# print(f"find: {find_position}")  # Output: 8

# # rfind: Return position of first character of last occurrence of substring in the string; returns -1 if not found
# s_repeated = "hello world world"
# rfind_position = s_repeated.rfind(substring)
# print(f"rfind: {rfind_position}")  # Output: 12

# # replace: Replace occurrences of string with another string
# replaced_string = s.replace("World", "Python")
# print(f"replace: {replaced_string}")  # Output: "  Hello Python  "

# # strip, rstrip, lstrip: Trim whitespace, including newlines
# stripped_s = s.strip()
# print(f"strip: {stripped_s}")  # Output: "Hello World"

# right_stripped_s = s.rstrip()
# print(f"rstrip: {right_stripped_s}")  # Output: "  Hello World"

# left_stripped_s = s.lstrip()
# print(f"lstrip: {left_stripped_s}")  # Output: "Hello World  "

# # split: Break string into list of substrings using passed delimiter
# split_s = s.strip().split(" ")
# print(f"split: {split_s}")  # Output: ['Hello', 'World']

# # lower: Convert alphabet characters to lowercase
# lower_s = s.lower()
# print(f"lower: {lower_s}")  # Output: "  hello world  "

# # upper: Convert alphabet characters to uppercase
# upper_s = s.upper()
# print(f"upper: {upper_s}")  # Output: "  HELLO WORLD  "

# # casefold: Convert characters to lowercase, and convert any region-specific variable character combinations to a common comparable form
# casefold_s = s.casefold()
# print(f"casefold: {casefold_s}")  # Output: "  hello world  "

# # ljust, rjust: Left justify or right justify, respectively; pad opposite side of string
# left_justified = s.strip().ljust(20, "*")
# print(f"ljust: {left_justified}")  # Output: "Hello World*********"

# right_justified = s.strip().rjust(20, "*")
# print(f"rjust: {right_justified}")  # Output: "*********Hello World"

import pandas as pd

# Sample DataFrame
data = {
    "Name": [" Alice ", "Bob", "Charlie", "David", "Eve "],
    "Email": [
        "alice@example.com",
        "BOB@EXAMPLE.COM",
        "charlie@Example.com",
        "DAVID@example.com",
        "EVE@example.com",
    ],
    "Text": [
        "  hello world  ",
        "sample TEXT",
        "Another Example",
        "lorem ipsum DOLOR",
        "  goodbye world  ",
    ],
    "Category": [" a|b|c ", " a|c|e ", " b|d|e ", "a|b|d", " c|e "],
}

df = pd.DataFrame(data)
print(df, "\n \n")

# Strip whitespace from 'Name' column
df["Name"] = df["Name"].str.strip()

# Convert 'Email' to lowercase
df["Email"] = df["Email"].str.lower()

# Replace ' ' with '-' in 'Text' column
df["Text"] = df["Text"].str.replace(" ", "-")

# Check if 'Text' column ends with a specific substring
df["EndsWith"] = df["Text"].str.endswith("world--")

# Split 'Category' column into multiple dummy columns
df["Category"] = df["Category"].str.strip().str.replace(" ", "").str.split("|")
dummies = df["Category"].apply(lambda x: pd.Series(1, index=x)).fillna(0)
df = df.drop(columns="Category").join(dummies.add_prefix("Category_"))

# Count occurrences of 'l' in 'Text' column
df["l_count"] = df["Text"].str.count("l")

# Check if 'Text' column starts with 'hello'
df["StartsWithHello"] = df["Text"].str.startswith("-hello")

# Find position of 'example' in 'Email' column
df["example_pos"] = df["Email"].str.find("example")

# Justify 'Name' to the left with padding
df["Name_ljust"] = df["Name"].str.ljust(10, "*")

# Display the cleaned DataFrame
print(df)
