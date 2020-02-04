#Write a program that print half star pattern for given number n. The following is pattern for n = 5.
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *

import sys
sys.stdout = open("output.txt", "w+")

a = 0
for i in range(1, 7):
    for j in range(1, (7 - i)):
        print(end=" ")

    while a != (i - 1):
        print("*", end="")
        a = a + 1
    a = 0

    print()

k = 1
a = 1
for i in range(1, 6):
    for j in range(1, k + 1):
        print(end=" ")
    k = k + 1

    while a <= ((5 - i)):
        print("*", end="")
        a = a + 1
    a = 1
    print()

sys.stdout.close()