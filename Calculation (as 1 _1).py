# Does calculaton by putting two numbers and the mathimatical sign to get the result

# input 2 values and store them in variables num1, num2, and the operator of choice
num1, operator, num2 = input('Enter the calculation: ').split()

# convert the string into an intiger
num1 = int(num1)
num2 = int(num2)

# print the results based on the condition
# if it is (+) add, and if it is (-) substract ...
if operator == '+':
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
elif operator == '-':
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
elif operator == '/':
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
elif operator == '*':
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
elif operator == '%':
    print('{} % {} = {}'.format(num1, num2, num1 % num2))
else:
    print('use the mathimatical signs +, -, /, %, or * next time')


