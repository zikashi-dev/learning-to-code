# PASSWORD CHECKER 

password = input("Enter your password: ")
length_ok = False
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "!@#$%^&*()-_+=<>?/"
# Check length
if len(password) >= 8:
    length_ok = True
# Check each character
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True
# Final decision
if length_ok and has_upper and has_lower and has_digit and has_special:
    print("✅ Strong Password")
else:
    print("❌ Weak Password")
    print("Password must contain:")
    if not length_ok:
        print("- At least 8 characters")
    if not has_upper:
        print("- An uppercase letter")
    if not has_lower:
        print("- A lowercase letter")
    if not has_digit:
        print("- A number")
    if not has_special:
        print("- A special character")
