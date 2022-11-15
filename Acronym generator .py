# Input
original_string = input("Insert a string to generate the acronym: ")

# Convert that string to uppercase for the acronym
original_string = original_string.upper()

# Convert the string into a list
list_of_words = original_string.split()

# Cycle through the list to get the first letter and eliminate the new line
for i_word in list_of_words:
    print(i_word[0], end="")

# To add the new line
print()