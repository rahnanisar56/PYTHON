try:
    name = input("Enter your name: ")
    feedback = input("Enter your feedback: ")

    if name == "":
        raise ValueError("Name cannot be empty.")

    if feedback == "":
        raise ValueError("Feedback cannot be empty.")

    print("\nThank you for your feedback!")
    print("Name:", name)
    print("Feedback:", feedback)

except ValueError as e:
    print("Error:", e)

finally:
    print("Feedback process completed.")