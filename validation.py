def account_number_validation(accountNumber):

    #if account_number_validation:
    
    if accountNumber:

            try:
                int(accountNumber)

                if len(str(accountNumber)) == 10:

                    return True
                else:
                    #print("Account Number cannot be less or more than 10 digits")
                    return False

            except ValueError:
                #print("Invalid Account Number, account number should be an integer")
                return False
            except TypeError:
                #print("Invalid account type")
                return False
    
    else:
        print("Account Number is a required field")
        return False


# def validation_registration_input(input):
#     # check if it's a list
#     # check each item in the list and be sure they are the correct data type

