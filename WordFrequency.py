#Question7. Word Frequency 
#a. Write a function called word_frequencies(myList) that accepts a list of strings called myList 
#and returns a dictionary where the keys are the words from myList and the values are the number of times that word appears in myList. 

#b. Write a function to invert key and value pairs in the dictionary you constructed. Sort the dictionary according to the new keys. 
#The function should accept a dictionary as parameter and return a tuple with the most frequent word and its frequency.


#a.
def wordFrequencies(myList):
    myDictionary = {}
    for x in myList:
        myDictionary[x] = myList.count(x)  
    return (myDictionary)    


myList = ["Hi","This","is","a","paragraph","Hi","This","is","python"]
print("Original list: ",myList)
myDict = wordFrequencies(myList)
print("Dictionary with word frequencies : ",myDict)

#b.


def invertDict(myDict):
    newDict = {}
    for key,value in myDict.items():
        newDict[value] = key
    return newDict

def sortDict(newDict):
    return[(i,newDict[i]) for i in sorted(newDict.keys())]

invertedDict = invertDict(myDict)
sortedDict = sortDict(invertedDict)

print("Sorted Dictionary: ",sortedDict)