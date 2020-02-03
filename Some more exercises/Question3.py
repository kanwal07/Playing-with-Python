#question3
#Write a program squares.py with a for loop that produces the following output: 1 4 9 16 25 36 49 64 81 100



# the question starts at 1 and increments with 1, calculating the square till 10
#pseudo-- take a number(starting with 1), print the square and increment it, repeat till reaching 10 ---  for loop


for i in range(1,11):  #doesn't include 11 but includes 1
    print(i**2, end=" ")