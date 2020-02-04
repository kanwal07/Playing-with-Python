#Consider an mxn grid. Write a function random_walk() that takes the number of rows and columns in the grid,
# simulates a radom_walk() starting in the center of the grid and computes the number of times 
# each intersection has been visited by the random walk. The center of the grid can be found by using
# the floor operator on m and n as such: m//2 and n//2. Output the result in a file.

import random
import sys
sys.stdout = open("output.txt", "a")

#rows = input("Enter number of rows: ")
#columns = input("Enter number of columns: ")

rows = 5
columns = 11

matrix = [[0 for i in range(int(columns))] for j in range(int(rows))]


n = int(columns)
m = int(rows)
cm = int(int(m)/2)
cn = int(int(n)/2)


matrix[cm][cn] = 1


counter = 0
while counter < random.randrange(10, 20):
    m1 = random.randrange(0, m)
    n1 = random.randrange(0, n)
    matrix[m1][n1] += 1
    counter += 1
print(matrix)

sys.stdout.close()