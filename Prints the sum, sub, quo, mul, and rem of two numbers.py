# ask the user to input 2 values and store them in variables num1 and num2
num1, num2 = input('Enter 2 numbers: ').split()

# convert the string into an intiger
num1 = int(num1)
num2 = int(num2)

# add the values
sum = num1 + num2

# substract
sub = num1 - num2

# multiply
mul = num1 * num2

# quotient
div = num1 / num2

# remainder
rem = num1 % num2

# print the results
print('{} + {} = {}'.format(num1, num2, sum))
print('{} - {} = {}'.format(num1, num2, sub))
print('{} * {} = {}'.format(num1, num2, mul))
print('{} / {} = {}'.format(num1, num2, div))
print('{} % {} = {}'.format(num1, num2, rem))


