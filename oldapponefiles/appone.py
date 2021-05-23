

from datetime import datetime
#from datetime import date

today = datetime.today()
#now = datetime.now()
#current_time = now.strftime("%H:%M:%S")

name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi', 'passwordMike','passwordLove']
userbalance = ['$200', '$300' , '$400']


if(name in allowedUsers) :
    password = input ("Your password? \n")
    userID= allowedUsers.index(name)
    
    if(password == allowedPassword[userID]):
        print('Your Password is correct')
        print('Welcome %s' % name)
        #print("Current Time =", current_time)
        print("Today's date:", today)
        print('these are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Compliant')

        selectedOption = int(input('Please select option:'))

        

        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            withdraw = input("How much would you like to withdraw?")
            print = ('your balance %s' % userbalance)
            print('Take your cash')
            print('these are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')
            #pass
        elif(selectedOption == 2):
            print('you selected %s'  % selectedOption)
            deposit = input("How much would you like to deposit?")
            #print('Your current balance is $50,000')
            #userbalance = [200 dollars, 300 dollars , 400 dollars]
            print = ('your balance %s' % userbalance)
            print('Thank you for your deposit')
            print('these are the available options:')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')

          
        elif(selectedOption == 3):
            print ('you selected %s'  % selectedOption)
            compliant = input('What is issue would you like to report?')
            print('Thank you for contacting us')
            print('1. Withdrawal')
            print('2. Cash Deposit')
            print('3. Compliant')
          

        elif(selectedOption > 3):
            print('you selected an invalid option, there are only 3 valid options, 1. Withdrawal, 2. Cash Deposit, 3. Compliant. The program will terminate now, try again with one of the 3 selections, thank you')

    else:
        print('Your password is incorrect, this transaction is terminated you will need to try again with a correct password, thank you')
      


else:
    print('Your Name is not found, as a result this transaction is terminated, please try again with name that is in our preselected acceptable username list, thank you')
    


