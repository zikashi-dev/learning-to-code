# Creating dictionaries
student = {
    "name": "Ali",
    "age": 18,
    "marks": 87.5,
    "is_passed": True
}
print("Student dictionary:", student)
# Accessing values
print("\nName:", student["name"])
print("Age:", student.get("age"))
# Using get() to avoid error
print("Grade:", student.get("grade", "Not Assigned"))
# Modifying values
student["age"] = 19
print("\nUpdated age:", student)
# Adding new key value pair
student["city"] = "Layyah"
print("After adding city:", student)
# Removing elements
student.pop("is_passed")
print("\nAfter pop:", student)
# Removing last inserted item
student.popitem()
print("After popitem:", student)
# Dictionary keys, values, items
print("\nKeys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())
# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)
# Checking membership
print("\nIs 'name' a key?", "name" in student)
print("Is 'grade' a key?", "grade" in student)
# Dictionary with mixed data
data = {
    1: "One",
    2: "Two",
    3: "Three"
}
print("\nNumber dictionary:", data)
# Nested dictionary
students = {
    "student1": {"name": "Ali", "marks": 85},
    "student2": {"name": "Sara", "marks": 92},
    "student3": {"name": "Ahmed", "marks": 78}
}
print("\nNested dictionary:")
for key, value in students.items():
    print(key, ":", value)
print("Student2 marks:", students["student2"]["marks"])
# Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print("\nSquares dictionary:", squares)
# Creating dictionary using fromkeys()
keys = ["math", "physics", "chemistry"]
subjects = dict.fromkeys(keys, 0)
print("\nSubjects dictionary:", subjects)
# Clearing dictionary
subjects.clear()
print("After clear:", subjects)
# Copying dictionary
copy_student = student.copy()
print("\nCopied dictionary:", copy_student)
