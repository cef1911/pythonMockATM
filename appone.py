# print ("Hello World")

from datetime import datetime
from datetime import date

today = date.today()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi', 'passwordMike','passwordLove']

#print (allowedUsers.index('Mike'))

if(name in allowedUsers) :
    password = input ("Your password? \n")
    userID= allowedUsers.index(name)
    
    if(password == allowedPassword[userID]):
        print('Welcome %s' % name)
        print("Current Time =", current_time)
        print("Today's date:", today)
        print('these are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Compliant')

        selectedOption = int(input('Please select option:'))

        #print(selectedOption == 1)

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            withdraw = input("How much would you like to withdraw?")
            print('Take your cash')
            print('these are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')
            #pass
        elif(selectedOption == 2):
            print('you selected %s'  % selectedOption)
            deposit = input("How much would you like to deposit?")
            print('Your current balance is $50,000')
            print('these are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')

           # pass
        elif(selectedOption == 3):
            print ('you selected %s'  % selectedOption)
            compliant = input('What is issue would you like to report?')
            print('Thank you for contacting us')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')
           # pass
    else:
        print('Invalid Option selected, please try again')

else:
    print('Name not found, please try again')

#print(username)