# Function practice
def greet_user(name):
    print("Hello,", name)
greet_user("Zikashi")

# Function returning multiple values
def calculate(a, b):
    sum_value = a + b
    product = a * b
    return sum_value, product
s, p = calculate(4, 6)
print("Sum:", s)
print("Product:", p)
