# Get the number of rows for the tree
# It needs to be an intigers because it's neccessary to do calculations
tree_height = eval(input("What is the height of the tree? "))

# Get the starting spaces for the top of the tree
# Because as the hashes go down it will also determine the column
spaces = tree_height -1

# There will be one hash at the start/top of the tree
hashes = 1

# The stump of the tree is same as the top
stump_spaces = tree_height - 1

# Use while to make sure the right number of rows are printed
while tree_height !=0:

# use end="" to print the spaces and make sure the process ends
    for i in range(spaces):
        print(' ', end="")

# Print the hashes
    for i in range(hashes):
        print('#', end="")

# New line will be created after each row is printed
    print()

# The number of hashes is incremented by 2 for each row
    hashes += 2

# The number of spaces is decremented by 1 for each row
    spaces -= 1

# tree_height is decremented each row to jump out of the loop
    tree_height -= 1

# Print space before hash and stumps
for i in range(stump_spaces):
    print(' ', end="")

print('#')