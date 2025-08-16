# This program takes users first and last name
# Concatenates the first and last name
# And displays a personalized greetings

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

#Using the string function title() to making the first char as caps
#useful in case user has input the name all in lower

full_name = f_name.title() + ' ' + l_name.title()

# Using f-string for formating.
print (f'Hello, {full_name}! Welcome to the Python program.' )