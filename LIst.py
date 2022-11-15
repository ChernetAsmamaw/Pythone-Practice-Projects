# Program that generates 5 random numbers within 0-9 range

import random
import math

number_list = []
for i in range(5):
    number_list.append(random.randrange(1, 10))

# List uses 0 index so to get the index number for each item in the list alone
i = len(number_list) - 1

# Swap values and store it in a temporary list
while i > 1:
    j = 0
    while j < 1:
        if number_list[j] > number_list[j + 1]:
            temp = number_list[j]
            number_list[j] = number_list[j + 1]
            number_list[j + 1] = temp
        else:
            print()
        j += 1
    i -= 1

# Prints separated by comma
for k in number_list:
    print(k, end=", ")
print()




