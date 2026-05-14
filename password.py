import random
import string

print("========== PASSWORD GENERATOR ==========")

while True:

    print("\nSelect Password Options:")
    print("1. Include Uppercase Letters")
    print("2. Include Lowercase Letters")
    print("3. Include Numbers")
    print("4. Include Symbols")

    characters = ""

    upper = input("\nInclude Uppercase Letters? (yes/no): ")
    lower = input("Include Lowercase Letters? (yes/no): ")
    numbers = input("Include Numbers? (yes/no): ")
    symbols = input("Include Symbols? (yes/no): ")

    if upper.lower() == "yes":
        characters += string.ascii_uppercase

    if lower.lower() == "yes":
        characters += string.ascii_lowercase

    if numbers.lower() == "yes":
        characters += string.digits

    if symbols.lower() == "yes":
        characters += string.punctuation

    if characters == "":
        print("\nPlease select at least one option.")
        continue

    length = int(input("\nEnter Password Length: "))

    password = ""

    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    again = input("\nDo you want to generate another password? (yes/no): ")

    if again.lower() != "yes":
        print("\nThank You for Using Password Generator!")
        break