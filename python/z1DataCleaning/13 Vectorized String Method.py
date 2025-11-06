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
print(df)

# Concatenate ID and Email columns
df["ID_Email"] = df["ID"].str.cat(df["Email"], sep=" | ")

# Check if Email contains 'example'
df["Contains_example"] = df["Email"].str.contains("example")

# Count occurrences of 'text' in the Text column
df["Text_count"] = df["Text"].str.count("text")

# Extract domain names from Email column
df["Domain"] = df["Email"].str.extract(r"@([\w\.]+)")

# Check if Text starts with 'Text'
df["Starts_with_Text"] = df["Text"].str.startswith("Text")

# Find all numbers in the Text column
df["Numbers"] = df["Text"].str.findall(r"\d+")

# Replace 'text' with 'TEXT' in the Text column
df["Text_replaced"] = df["Text"].str.replace("text", "TEXT")

# Trim whitespace from the Text column
df["Text_trimmed"] = df["Text"].str.strip()

# Convert Text column to uppercase
df["Text_upper"] = df["Text"].str.upper()

# Display the cleaned DataFrame
print(df)

# Table of Vectorized String Methods
# Method	Description
# cat	Concatenate strings element-wise with an optional delimiter.
# contains	Return a boolean array indicating if each string contains a pattern/regex.
# count	Count occurrences of a pattern.
# extract	Use a regular expression with groups to extract one or more strings from a Series of strings. The result is a DataFrame with one column per group.
# endswith	Equivalent to x.endswith(pattern) for each element.
# startswith	Equivalent to x.startswith(pattern) for each element.
# findall	Compute a list of all occurrences of a pattern/regex for each string.
# get	Index into each element (retrieve the i-th element).
# isalnum	Equivalent to built-in str.isalnum.
# isalpha	Equivalent to built-in str.isalpha.
# isdecimal	Equivalent to built-in str.isdecimal.
# isdigit	Equivalent to built-in str.isdigit.
# islower	Equivalent to built-in str.islower.
# isnumeric	Equivalent to built-in str.isnumeric.
# isupper	Equivalent to built-in str.isupper.
# join	Join strings in each element of the Series with the passed separator.
# len	Compute the length of each string.
# lower, upper	Convert cases; equivalent to x.lower() or x.upper() for each element.
# match	Use re.match with the passed regular expression on each element, returning matched groups as a list.
# pad	Add whitespace to the left, right, or both sides of strings.
# center	Equivalent to pad(side='both').
# repeat	Duplicate values (e.g., s.str.repeat(3) is equivalent to x * 3 for each string).
# replace	Replace occurrences of a pattern/regex with some other string.
# slice	Slice each string in the Series.
# split	Split strings on a delimiter or regular expression.
# strip	Trim whitespace from both sides, including newlines.
# rstrip	Trim whitespace on the right side.
# lstrip	Trim whitespace on the left side.
