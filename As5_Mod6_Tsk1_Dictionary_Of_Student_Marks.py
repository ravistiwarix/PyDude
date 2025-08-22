# Program creates a dictionary of students where name is key and marks is value.
# It takes student name from the user.
# The program then Retrieves and displays the corresponding marks.
# And, if the student’s name is not found, displays an appropriate message.

stud = {
    "Ravi": {"Marks": 81},
    "John": {"Marks": 91},
    "Alice": {"Marks": 72},
    "Meena": {"Marks": 93},
    "Rajesh": {"Marks": 64}
}

#capitalize() function has been used to match the case.
nm =input("Enter the student's name: ").capitalize()

if nm in stud:
    print(f"{nm}'s marks: ",stud[nm]['Marks'])
else:
    print("Student not found.")