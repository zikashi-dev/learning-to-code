
# Creating tuples
t1 = (1, 2, 3, 4, 5)
t2 = ("Ali", "Ahmed", "Sara")
t3 = (10,)   # single-element tuple

print("Tuple t1:", t1)
print("Tuple t2:", t2)
print("Single element tuple:", t3)

# Accessing tuple elements
print("\nFirst element of t1:", t1[0])
print("Last element of t2:", t2[-1])

# Slicing tuples
print("\nSlice (1 to 3):", t1[1:4])

# Looping through tuple
print("\nLooping through tuple:")
for item in t2:
    print(item)

# Tuple methods
print("\nCount of 2 in t1:", t1.count(2))
print("Index of 3 in t1:", t1.index(3))

# Tuple packing and unpacking
person = ("Ali", 18, "Pakistan")
name, age, country = person

print("\nUnpacked values:")
print("Name:", name)
print("Age:", age)
print("Country:", country)

# Tuple with mixed data
mixed_tuple = (1, "Python", True, 3.14)
print("\nMixed tuple:", mixed_tuple)

# -------------------- SETS --------------------

# Creating sets
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7}

print("\nSet s1:", s1)
print("Set s2:", s2)

# Sets automatically remove duplicates
s3 = {1, 2, 2, 3, 3, 4}
print("Set with duplicates removed:", s3)

# Adding elements
s1.add(10)
print("\nAfter add:", s1)

# Updating set
s1.update([8, 9])
print("After update:", s1)

# Removing elements
s1.remove(3)
print("\nAfter remove 3:", s1)

# Discard does not raise error
s1.discard(100)
print("After discard 100:", s1)

# Set operations
print("\nUnion:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference (s1 - s2):", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

# Membership test
print("\nIs 5 in s1?", 5 in s1)

# Looping through set
print("\nLooping through set:")
for item in s1:
    print(item)

# Set comprehension
even_set = {x for x in range(1, 11) if x % 2 == 0}
print("\nEven numbers set:", even_set)

# Converting list to set
list_numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(list_numbers)

print("\nUnique numbers from list:", unique_numbers)
