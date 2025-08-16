#This program takes an integer input from the user
# Check if the number is even or odd and displays the result accordingly

num=int(input("Enter a number: "))

#Usig modulo operator (%) to the remainder.
rem = num % 2

if rem == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")