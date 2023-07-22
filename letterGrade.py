# logical/comparision operator diye **Short-circuit and-orlogical
marks1 = float(input('Enter your marks1: '))
marks2 = float(input('Enter your marks2: '))

if 80 <= marks1 <= 100:
    print('He got A+')
elif 70 <= marks1 <= 80:
    print('He got A')
else:
    print('He got', marks2)
