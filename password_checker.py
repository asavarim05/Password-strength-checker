import re

print("==== Password Strength Checker ====")

password = input("Enter your password: ")

score = 0

# Check length
if len(password) >= 8:
    score += 1
    print("✔ Good length")
else:
    print("✖ Password too short")

# Check uppercase
if re.search("[A-Z]", password):
    score += 1
    print("✔ Contains uppercase letter")
else:
    print("✖ Missing uppercase letter")

# Check lowercase
if re.search("[a-z]", password):
    score += 1
    print("✔ Contains lowercase letter")
else:
    print("✖ Missing lowercase letter")

# Check number
if re.search("[0-9]", password):
    score += 1
    print("✔ Contains number")
else:
    print("✖ Missing number")

# Check special characters
if re.search("[!@#$%^&*()]", password):
    score += 1
    print("✔ Contains special character")
else:
    print("✖ Missing special character")

# Final result
print("\nPassword Strength:")

if score <= 2:
    print("Weak")
elif score <= 4:
    print("Medium")
else:
    print("Strong")