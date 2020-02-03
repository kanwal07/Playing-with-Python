#2. Boolean expressions. Do not use conditionals.
#a. Write a function is_leapyear() that returns True if a year is a leap year, and False otherwise. A leap year is
#divisible by 400 or by 4 but not by 100.
#b. Write a function is_vowel() that returns True or False depending on whether its arguments is a vowel or
#consonant. 


#a.
 
def is_leapYear(year):
    temp = (((year % 4 == 0) or (year % 400 == 0)) and (year % 100 != 0))
    print (temp)

 
#year = int(input("Enter the year to be checked(leap year=true and not leap year=false): "))

#is_leapYear(year)



#b.

def is_vowel(args):
    args = args.upper()
    temp = (args == 'A' or args == 'E' or args == 'I' or args == 'O' or args == 'U')
    print (temp)

args = input("Enter a letter(true=vowel and false=consonant): ")
is_vowel(args)