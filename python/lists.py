# Creating lists
numbers = [1, 2, 3, 4, 5]
names = ["Ali", "Ahmed", "Sara"]
mixed = [1, "Python", True, 3.5]

print("Numbers:", numbers)
print("Names:", names)
print("Mixed:", mixed)

# Accessing elements
print("\nFirst number:", numbers[0])
print("Last name:", names[-1])

# Slicing
print("\nSlice (index 1 to 3):", numbers[1:4])
print("Reverse list:", numbers[::-1])

# Modifying elements
numbers[2] = 99
print("\nModified numbers:", numbers)

# Adding elements
numbers.append(6)
print("After append:", numbers)

numbers.insert(1, 100)
print("After insert:", numbers)

# Extending list
numbers.extend([7, 8, 9])
print("After extend:", numbers)

# Removing elements
numbers.remove(99)
print("\nAfter remove:", numbers)

popped_item = numbers.pop()
print("Popped item:", popped_item)
print("After pop:", numbers)

# List length
print("\nLength of numbers:", len(numbers))

# Sorting
numbers.sort()
print("Sorted list:", numbers)

numbers.sort(reverse=True)
print("Reverse sorted:", numbers)

# Looping through a list
print("\nLooping through names:")
for name in names:
    print(name)

# Using range with list
squares = []
for i in range(1, 6):
    squares.append(i * i)
print("\nSquares list:", squares)

# List comprehension
cubes = [i**3 for i in range(1, 6)]
print("Cubes using comprehension:", cubes)

# Checking membership
print("\nIs 4 in numbers?", 4 in numbers)
print("Is 'Ali' in names?", "Ali" in names)

# Nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\nMatrix:")
for row in matrix:
    print(row)
print("Element at row 2, column 3:", matrix[1][2])

# Copying lists
copy_numbers = numbers.copy()
print("\nCopied list:", copy_numbers)

# Clearing list
copy_numbers.clear()
print("After clear:", copy_numbers)
