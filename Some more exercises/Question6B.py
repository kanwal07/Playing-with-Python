#Question6B
#Write a function positive_min(lf) that returns the smallest positive float in the list lf

#pseudo- take a list of floats, 
# assign the first number as the smallest number, 
# traverse through the list and compare the smallest number with each element in the list, 
# if the smallest element if negative, skip it
# replace the smallest number with the one which is less of the two,
# print the smallest of the all in the end

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

#taking 4 random float numbers
floatList = [round(random.uniform(-10,10),2),round(random.uniform(-10,10),2),round(random.uniform(-10,10),2),round(random.uniform(-10,10),2)]

print ("The list of floats is: ", floatList)

positive_min(floatList)