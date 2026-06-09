import os

n = int(input("How many student names do you want to add? "))

file = open("students.txt", "a")

for i in range(n):
    name = input(f"Enter student name {i+1}: ")
    file.write(name + "\n")

file.close()

if os.path.exists("students.txt"):
    print("\nExisting Student Names:")
    
    file = open("students.txt", "r")
    for line in file:
        print(line.strip())
    file.close()
else:
    print("\nNo existing student records found.")

print("\nUpdated List of Student Names:")

file = open("students.txt", "r")
for line in file:
    print(line.strip())
file.close()