# Program creates a list of numbers from 1 to 10.
# Extracts the first five elements from the list.
# Reverses these extracted elements.
# Prints both the extracted list and the reversed list
# Program demonstrates multiple ways to reverse a list using reverse(), Slicing, reversed(), pop()

orig_list=[1,2,3,4,5,6,7,8,9,10]     # Original list
new_list=orig_list[0:5]              # New list having first five elements of original list

#Print Original List
print("Original list: ", orig_list)

# Print sliced list
print("Extracted first five elements: ",new_list)

#--------- Method #1 Using reverse() function --- Start
rev_list=orig_list[0:5]
rev_list.reverse()
print("\nReversed extracted elements (using reverse()): ",rev_list)
#--------- Method #1 Using reverse() function --- End

#--------- Method #2 Using Slicing --- Start
# list[start : stop : step]
reversed_list_slice= orig_list[4::-1]
print("\nReversed extracted elements (using Slicing): ",reversed_list_slice)
#--------- Method #2 Using Slicing --- End

#--------- Method #3 Using reversed() with list() --- Start
reversed_list_reversed= list(reversed(new_list))
print("\nReversed extracted elements (using reversed()): ",reversed_list_reversed)
#--------- Method #3 Using reversed() with list() --- End

#--------- Method #4 Using pop() --- Start
# Reversing a list using - pop()
# Pop() removes one element from the end and returns it.
rev_list_pop=[]
while new_list:
    # print(new_list.pop())
    rev_list_pop.append(new_list.pop())

print("\nReversed extracted elements (using pop()): ",rev_list_pop)

#--------- Method #4 Using pop() --- End



