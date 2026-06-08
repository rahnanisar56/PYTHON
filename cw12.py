import re

try:
    title = input("Enter book title: ")
    year = input("Enter publication year: ")

    if re.fullmatch(r"[A-Za-z ]+", title):
        print("Valid book title")
    else:
        raise ValueError("Book title should contain only alphabets and spaces.")

    if re.fullmatch(r"(19|20)\d{2}", year):
        print("Valid publication year")
    else:
        raise ValueError("Publication year must be a 4-digit number starting with 19 or 20.")

    print("\nBook Details")
    print("Title :", title)
    print("Year  :", year)

except ValueError as e:
    print("Error:", e)

finally:
    print("Library system process completed.")