def pwd_check():
    
    check_flag = False

    while(check_flag == False):
        password = input("Enter a valid password... ")
        if(len(password) < 8):
            return("The password should have at least 8 characters")
        elif not any (password.isdigit() for password in password):
            return("The password should have at least 1 digit")
        elif not any (password.isupper() for password in password):
            return("The password should have at least 1 upper case letter")
        elif not any (password.islower() for password in password):
            return("The password should have at least 1 lower case letter")
        elif (password.isalnum() == True):
            return("The password should have at least 1 alpha num")
        else:
            check_flag == True
            return("Your password is strong!")
            
