# This program reads a test file name sample.txt
# Print its content line by line.
# If the fie does not exist handles errors gracefully

fname="sample.txt"    #File name
try:
    f = open(fname,"r")

except FileNotFoundError:
    print(f"The file {fname} was not found.")

else:
    for line in f:
        print(line.strip()) # strip() removes extra \n at the end
    f.close()