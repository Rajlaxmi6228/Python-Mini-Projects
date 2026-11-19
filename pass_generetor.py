import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for i in range(length):
        password += random.choice(characters)
    return password


print("-----RANDOM PASSWORD GENERATOR-----")

try:

    length = int(input("Enter length of password: "))
    if length < 4:
        print("Length should be at least of 4 characters.")
    else:
        pwd = generate_password(length)
        print("password generated:",pwd)
except:
    print("An error occured.")
