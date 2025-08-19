# This program takes user input and writes it to a file named 'output.txt'.
# Appends additional data to the same file.
# Reads and displays the final content of the file.

fn='output.txt'        #File name
with open(fn,'a+') as f1:
    txt1=input("Enter text to write to the file: ")

    f1.write(txt1)
    f1.write('\n')
    print(f"Data successfully written to {fn}.")

    txt2=input("\nEnter aditional text to append: ")
    f1.write(txt2)
    f1.write('\n')
    print("Data successfully appended.")

# Opening the file in read mode to display the content
print(f"\nFinal content of {fn}:")
f2=open(fn,'r')
print(f2.read())
f2.close()


