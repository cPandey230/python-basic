import re

# # Sample text
# text = "The quick brown fox jumps over the lazy dog. The fox is quick and smart."

# # findall
# pattern = r"\b\w{4}\b"  # Finds all 4-letter words
# result = re.findall(pattern, text)
# print("findall:", result)

# # finditer
# result_iter = re.finditer(pattern, text)
# print("finditer:", [match.group() for match in result_iter])

# # match
# pattern = r"The"
# result = re.match(pattern, text)
# print("match:", result.group() if result else None)

# # search
# pattern = r"fox"
# result = re.search(pattern, text)
# print("search:", result.group() if result else None)

# # split
# pattern = r"\s+"  # Split by whitespace
# result = re.split(pattern, text)
# print("split:", result)

# # sub
# pattern = r"fox"
# replacement = "cat"
# result = re.sub(pattern, replacement, text)
# print("sub:", result)

# # subn
# pattern = r"quick"
# replacement = "fast"
# result, num_subs = re.subn(pattern, replacement, text)
# print("subn:", result, "- Substitutions made:", num_subs)


import pandas as pd

# Sample DataFrame
data = {
    "ID": ["abc123", "def456", "ghi789"],
    "Email": ["test.email@example.com", "another.email@domain.org", "user@website.net"],
    "Text": [
        "This is a sample text.",
        "Another example text here.",
        "Text with numbers 123 and symbols #!@.",
    ],
}


df = pd.DataFrame(data)
print(f"{df}\n \n ")

# Extract domain names from Email column
df["Domain"] = df["Email"].str.extract(r"@([\w\.]+)")

# Find all numbers in the Text column
df["Numbers"] = df["Text"].apply(lambda x: re.findall(r"\d+", x))

# Replace all non-alphanumeric characters in the Text column
df["CleanText"] = df["Text"].apply(lambda x: re.sub(r"\W+", " ", x))

# Display the cleaned DataFrame
print(df)
