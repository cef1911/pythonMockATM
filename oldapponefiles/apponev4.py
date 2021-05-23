from datetime import datetime
today = datetime.today()
name = input("What is your name? \n")
allowedUsers = ['Seyi','Mike','Love']
allowedPassword = ['passwordSeyi', 'passwordMike','passwordLove']
currentBalance = 0
if(name in allowedUsers):
   password = input ("Your password? \n")
   userID= allowedUsers.index(name)
   if(password == allowedPassword[userID]):
       print('Your Password is correct')
       print('Welcome %s' % name)
       print("Today's date:", today)
       selectedOption = 1
       while selectedOption < 4:
           print('these are the available options:')
           print('1. Withdrawal')
           print('2. Cash Deposit')
           print('3. Compliant')
           print('4. Enter any other key to exit')
           selectedOption = int(input('Please select option:'))
           if selectedOption == 1:  
               print('you selected %d' % selectedOption)
               withdraw = float(input("How much would you like to withdraw?"))
               print('Take your cash')
           elif selectedOption == 2:
               print('you selected %d'  % selectedOption)
               print('your balance %d' % currentBalance)
               deposit = int(input("How much would you like to deposit?")) #100
               currentBalance = currentBalance + deposit 
               print("Your current balance is ", currentBalance)
           elif selectedOption == 3 :
               print ('you selected %d'  % selectedOption)
               compliant = input('What is issue would you like to report?')
               print('Thank you for contacting us')
           else:
               break
   else:
      print('Your password is incorrect, this transaction is terminated you will need to try again with a correct password, thank you')
else:
    print('Your Name is not found, as a result this transaction is terminated, please try again with name that is in our preselected acceptable username list, thank you')