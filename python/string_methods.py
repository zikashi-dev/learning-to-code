text = "  Hello Python World  "
# Length of string
print(len(text))
# Convert to lowercase
print(text.lower())
# Convert to uppercase
print(text.upper())
# Remove leading and trailing spaces
print(text.strip())
# Replace text
print(text.replace("Python", "Programming"))
# Find a word
print(text.find("World"))
# Check methods
print(text.startswith("Hello"))
print(text.endswith("World"))
# Split string into list
words = text.split()
print(words)
# Join list into string
joined_text = "-".join(words)
print(joined_text)
# Capitalize first letter
print(text.capitalize())
# Title case
print(text.title())
