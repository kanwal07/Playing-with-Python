#question1
#Write a program that reads 3 integers from the command line and assigns the read values to variables a, b, and c. 
# Write an expression inorder that evaluates to True if the numbers are either in ascending or descending order, and False otherwise.

#pseudo - 1. take input 3 numbers    2. find the largest    3. find the smallest  4. print the result

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def largestNum(num1,num2,num3):
    if(num1 >= num2 and num1 >= num3):
        return num1
    elif(num2 >=num1 and num2 >= num3):
        return num2
    else:
        return num3


def smallestNum(num1,num2,num3):
    if(num1 <= num2 and num1 <= num3):
        return num1
    elif(num2 <= num1 and num2 <= num3):
        return num2
    else:
        return num3

def inOrder(large,small,num1,num2):
    if(num1 == large and num2 == small):
        print ("True, The numbers are in decreasing order.")
    elif(num2 == large and num1 == small):
        print ("True, The numbers are in increasing order.")
    else:
        print ("False, The numbers are in no order.")    
    
largest = largestNum(a,b,c)
smallest = smallestNum(a,b,c)
inOrder(largest,smallest,a,c)
    