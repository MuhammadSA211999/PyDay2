num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))
num3 = float(input('Enter third number: '))

# check biggest number by condition
if (num1 > num2 and num2 > num3):
    if (num1 > num3):
        print(num1, 'is biggest number')
elif (num2 > num1 and num1 > num3):
    if (num2 > num3):
        print(num2, 'is biggest number')
else:
    print(num3, 'is biggest number')
