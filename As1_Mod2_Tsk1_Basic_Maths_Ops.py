# This python program takes two numbers from user
# and performs basic mathematical operations
# Addition, Subtraction, Multiplication, Division

n1 = int(input("Enter the first number: "))
#n2 = int(input("Enter the second number: "))
n2 = input("Enter the second number: ")
n2 = int(n2)

add_res = n1+n2
sub_res = n1-n2
mul_res = n1*n2
div_res = float(n1/n2)

print("Addition: ",add_res)
print("Subtraction: ",sub_res)
print("Multiplication: ",mul_res)
print ("Division: ",div_res)
