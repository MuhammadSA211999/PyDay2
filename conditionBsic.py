# check user grade by input's value
marks = float(input('Enter yor marks: '))

if (marks >= 90):
    print('You got A++')
elif (marks >= 80):
    print('You got just A+')
elif (marks >= 70):
    print('You got A')
elif (marks >= 60):
    print('You got A-')
elif (marks >= 50):
    print('You got B')
elif (marks >= 40):
    print('You got C')
else:
    print('You failed')
