# The user enters their investment
# Each year the investment will increase by the interest rate
# The values have to be converted to float


Investment = input('Enter Investment Amount: ')
Investment = float(Investment)

Interest_Rate = input('Enter the Interset Rate in persentage:')
Interest_Rate = float(Interest_Rate) * .01

for i in range(10):
    Investment = Investment + (Investment * Interest_Rate)

print('Investment after 10 years: {:.2f}'.format(Investment))