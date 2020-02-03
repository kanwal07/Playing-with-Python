#Question7
#Create a list (in one line) to return the multiplication table for an integer entered by the user. 
# For example, if the user enters 5 then the output should be: 
# [5, 1, 5] 
# [5, 2, 10] 
# [5, 3, 15] 
# . 
# .
# . 
# [5, 10, 50]
#Hint: the list is a list of lists

#pseudo -  take the input from the user, 
# make a list with elements as userInput, multiplication number, multiplication result, 
# store this list into another list- result list, 
# print result list 



number = int(input("Enter a number: "))
multipyList = []
resultList = []

for i in range(1,11):
    multiplyList = [number, i, number*i]
    resultList.append(multiplyList)

for element in resultList:
    print (element)