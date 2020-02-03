import random
import string
import module


#Function to check the strength of the password entered
            

#Function to generate a random password
def random_pwd():
    password = string.ascii_letters + string.digits + string.punctuation
    print("Your secure password is ")
    return( ''.join(random.choice(password) for i in range(1,10)))


#Function to encrypt the username and password
def Caesar_cipher(passwordText):
    encrypted_pass = ""
    for i in range(len(passwordText)):
        letter = passwordText[i]
        if(letter.isupper() and letter.isalpha()):
            encrypted_pass += chr((ord(letter) + 3 - 65) % 26 + 65)
        elif(letter.islower() and letter.isalpha()):
            encrypted_pass += chr((ord(letter) + 3 - 97) % 26 + 97)
        else:
            encrypted_pass += letter
    return encrypted_pass




#User inputs
choice = 'n'

while(choice != 'A' or choice != 'B'):
    print("Enter 'a' if you want to choose your password")
    print("Enter 'b' if you want to generate a random password")

    choice = input("Your choice... ")
    choice = choice.upper()

    if(choice == 'A'):
        password = module.pwd_check()
        print(password)
        break
    elif(choice == 'B'):
        password = random_pwd()
        print(password)
        break
    else:
        print("Please choose correct option.")




website = input("Enter the name of the website... ")
username = input("Enter the username... ")
username = Caesar_cipher(username)
password = Caesar_cipher(password)

threeTuple = ("Website : ", website, "Username : ", username, "Password : ", password)

f = open("my_passwords.csv", "w+")
for t in threeTuple:
    f.write(t)
f.close()

print("The details have been saved in my_password.csv file")
