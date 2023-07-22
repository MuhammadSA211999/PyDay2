# 1-100 porzonto while loop diye print
''''
W**hile loop structure**      example
i for initialization         i=1
keyword While, condition     while i>=10
statement                     print(i)
update intialize value       i=i+1

'''

# i = 1
# while i <= 100:
#     print(i)
#     i = i+1
# print('Programme end at 100')


# 1-100 porzonto **Even number print kora
# i = 1
# while i <= 100:
#     even = i % 2
#     if (even == 0):
#         print(i)
#     i = i+1
# print('printed even number')

# 1-100 porzonto Odd number print kora
# i = 1
# while i <= 100:
#     odd = i % 2
#     if (odd > 0):
#         print(i)
#     i += 1
# print('Odd number printed')


# print odd number to given
# efficents method

# number1 = int(input('Enter your number'))
# i = 1
# while i <= number1:
#     print(i)
#     i = i+2
# print('Prited odd nuber')

# print even number
# number2 = int(input('Enter the last digit: '))
# i = 2
# while i <= number2:
#     print(i)
#     i = i+2
# print('Even number is printed')

# 1-input number porzonto Jor/Bijor number er somosthi
number = int(input('enter your number: '))

evenSum = 0
i = 2
while i <= number:
    evenSum = evenSum+i
    i = i+2
print(evenSum)

oddSum = 0
i = 1
while i <= number:
    oddSum = oddSum+i
    i = i+2
print(oddSum)
print(evenSum+oddSum)
