#Question 3. List comprehension 
#a. Use list comprehension to output 5 random numbers between 1 and 1000, divisible by 5 and 7. 
#b. Use list comprehension to print a list after deleting even numbers.


#a.

import random

print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0],5))


#b.

def deleteEven(myList):
    for i in myList:
        if i%2==0:
            myList.remove(i)

myList = [1,2,3,4,5,6,7,8,9,0]

print("Original List : ",myList)
deleteEven(myList)
print("Updated List : ",myList)