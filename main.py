#functions


#Main Program

print('Welcome to Less Than Ten')
print('Please enter a value')
usrInput = ''

usrValues = []
proceed = 1
while proceed != 0:
    usrInput = input('Value or 0 to End: ')
    if not usrInput.isdecimal():
        print('{} is not a valid value.'.format(usrInput))
        proceed = ''
    elif int(usrInput) == 0:
        proceed = 0
    elif usrInput.isdecimal() and int(usrInput) > 0:
        usrValues.append(usrInput)
        proceed = ''


#Process list and
for i in range(len(usrValues)):
    if int(usrValues[i]) < 10:
        print('{} is less than 10.'.format(usrValues[i]))
    else:
        print('{} is not less than 10.'.format(usrValues[i]))
