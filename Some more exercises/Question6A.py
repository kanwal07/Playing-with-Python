#question6A
#Write a function strings2float(ls) that takes a list of strings ls and returns a list of floats.
#Your function should construct the list of floats to return, and not modify the list passed in.

#pseudo - take a list of strings and an empty float list, 
# find the length of the string list and append that many random float numbers to the empty float list


import random

def strings2float(stringList):
    
    for i in range (len(stringList)):     
        floatList.append(round(random.uniform(1,10),2))

    print(floatList)


stringList = ["Hi","Hello","Bonjour","Salut"]
floatList = []

strings2float(stringList)