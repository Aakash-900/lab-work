#
number = int(input("Enter a number"))
sum_digits = 0
for digit in str(number):
    sum_digits +=int(digit)
print(sum_digits)
