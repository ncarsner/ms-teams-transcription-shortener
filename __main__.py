import re

pattern = r"(\d.*)\r?\n(^[A-Z|+].*)\r?\n(\w.+)"

patterns = {
    # all matching groups
    # r"(\d.*)\r?\n(^[A-Z|+].*)\r?\n(\w.+)": r"\1\2\3",
    r"(\d.*)": r"\1",
    # r"(?<=\d{2}:\d{2}:\d{2}.\d{3} --> \d{2}:\d{2}:\d{2}.\d{3}\n)(^[A-Z|\W].*)": r"\2",
    r"(?<=.\d{3}\n)(^[A-Z|\W].*)": r"\2",
    r"(.*)\n(?=\d{2}:)": r"\3",
}


with open("sample_transcript_1.txt") as file:
    content = file.read()
    print(content)


# def transform_name(name):
#     for pattern, replacement in patterns.items():
#         if re.match(pattern, name, flags=re.IGNORECASE | re.DOTALL):
#             return replacement(re.match(pattern, name))

# print(transform_name(content))


# Function to format each match
def format_match(m):
    return f"Timestamp: {m.group(1)}, Speaker: {m.group(2)}, Content: {m.group(3)}"


# Use re.sub to apply format_match function to each match
formatted_output = re.sub(
    pattern, format_match, content, flags=re.MULTILINE | re.DOTALL
)

# Using re.sub with a lambda function for formatting
formatted_output = re.sub(
    pattern,
    lambda m: f"Timestamp: {m.group(1)}, Speaker: {m.group(2)}, Content: {m.group(3)}",
    content,
    flags=re.MULTILINE | re.DOTALL,
)

# Split and print each formatted line
for line in formatted_output.splitlines():
    if line.strip():  # This removes empty lines
        print(line)
