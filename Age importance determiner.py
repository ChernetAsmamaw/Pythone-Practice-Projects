# differnet ages will be enterd and the program decides eligability for travel
# 1 - 18 -> eligable
# 21, 50 > 65 -> eligable
# all others are not elegible


# recives the number of age and stores it in age
# eval() automatically turns input into intiger
age = eval(input("Enter age: "))

# and: if both conditions are true it returns true
# or: if either conditions are true it returns true
# not: converts true into false (if true you get false)

# age greater than or equal to 1 and less than or equal to 18 is eligable
# if the person is 21 or 50 is eligable
# if the person is less than 65 convert truth into false and vise versa

if (age >= 1) and (age <= 18):
    print("The person is eligable")
elif (age == 21) or (age == 50):
    print("The person is eligable")
elif not(age < 65):
    print("The person is eligable")
else:
    print("Sorry! but the person is not eligable")