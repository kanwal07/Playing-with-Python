A. Write a program my_passwords.py that offers the user the following options:
a. Check whether or not a password entered by the user is “good”, or
b. Generate a random password instead.

If (a) is selected, write a function pwd_check() that reads a string from the command line and checks whether or not it is a “good” password. 
A “good” password has the following criteria:
o It is at least 8 characters long
o It contains at least one digit (0-9)
o It contains at least one upper case letter (A-Z)
o It contains at least one lower case letter (a-z)
o It contains at least one non-alphanumeric character
If (b) is selected, write a function random_pwd() that generates a random password. 
Use the same criteria as above to generate a “good” password.

B. Write a function Caesar_cipher() that partially encrypts the password using a Caesar cipher. 
A Caesar cipher replaces each letter (and letters only) by the letter that is k positions ahead of it – and you wrap around if needed. 
The table below gives the Caesar cipher for k = 3.
ALPHABET
A B C D E F G H J I K L M N O P Q R S T U V W X Y Z
a b c d e f g h I j k l m n o p q r s t u v w x y z
CAESAR CIPHER
D E F G H J I K L M N O P Q R S T U V W X Y Z A B C
d e f g h I j k l m n o p q r s t u v w x y z a b c
For instance, if a password is 7gK?5-Qu and k = 3, the function should return 7jN?5-Tx

C. Modify the program to ask the user for which service or website s/he is needs the password and the associated user-name.
Encrypt the user-name using the Caesar_cipher() function above and save the 3-tuple in a file my_passwords.csv