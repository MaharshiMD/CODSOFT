import random
import string

print("Password Generator")

try:
    length = int(input("Enter password length: "))

    if length <= 0:
        print("Password length must be greater than zero.")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("Generated Password:", password)

except:
    print("Please enter a valid number.")
