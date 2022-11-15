# It hides a string entered as secrete code using numbers by unicode

normal_string = input('Enter a string to be hidden: ')

# To store the secrate message

secret_string = ""

# Cycle through each character in the string

for chr in normal_string:

#  store each character in the secret_string
# str converts it to a string
# ord converts the number or character code it gets into a string

# Subtract - 23 becaue the unicode for lower case goes up to 122 so
    secret_string += str(ord(chr) - 23)

# Prints out the secret message

print("The secret message is: ", secret_string)

# Cycles through each character code 2 at a time by incrementing by 2 each time
# 0 to len(seceret_string) is the range of every letter
# -1 because the first letter is seen as 0, so on the total from len there is 1 uneccessary spot
# 2 because we want it in a pair of two, since it takes two numbers to make one unicode

normal_string = ""
for i in range(0, len(secret_string)-1, 2):

    #Get the 1st and the 2nd for the two-digit numbers

    chraracter_code = secret_string[i] + secret_string[i+1]

    # Convert the code into characters and add them togather

    normal_string += str(int(chraracter_code) +23)

# Print the orignal mesaage
print("Orignal message :", normal_string)