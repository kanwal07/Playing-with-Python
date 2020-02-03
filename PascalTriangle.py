#5. Pascal Triangle
#Write a program that prompts the user for an integer and builds and prints the equivalent Pascal triangle.


import math


def combination(n, r): 
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))

def pascalTriangle(rows):
    result = [] 
    for count in range(rows):
        row = []
        for element in range(count + 1): 
            row.append(combination(count, element))
        result.append(row)
    return result

userInput = int(input("Enter a number: "))
for row in pascalTriangle(userInput):
    print(row)