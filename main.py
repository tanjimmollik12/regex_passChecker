# Password Checker
# Minimum 6 char,
# Start with number,
# can use: letters, numbers, @#$%
import re
password = input("Enter a password: ")
pattern = re.compile(r"\d[a-zA-Z0-9@#$%]{6,}")

b = pattern.fullmatch(password)

try:
    if b.group() != None:
        print("Password is valid.")
except AttributeError:
    print("Password does not meet criteria.")
