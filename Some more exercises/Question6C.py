#question6C
#Write a program minipos.py that reads a list of floats from the command line and prints the smallest positive value.

#pseudo- take a few floats from the user, 
# put them somehow in a list,
#compare the elements of the list


import random

def positive_min(floatList):
    small = floatList[0]
    for i in range (len(floatList)):
        if(floatList[i] < small):
            if(floatList[i]<0): #skip negative values
                continue
            small = floatList[i]
        else:
            small = small
    
    print ("The smallest positive float number in the list is: ", small)



# take input - string
input = input("Enter a list of float values separated be spaces: ")

# put input into list - strings
floatList = input.split()

#convert string list to float list
for i in range (len(floatList)):
    floatList[i] = float(floatList[i])

#print(type(floatList[0]))

positive_min(floatList)

