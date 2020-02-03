#Question 4. Shuffle
#Write a program that reads a sentence from the command line as a list of strings and returns the sentence in a shuffled order.
#The strings in the list need to change positions in place: do not create a duplicate list.

import random

listOfStrings = ["Write", "a", "program", "that", "reads", "a", "sentence", "from", "the", "command", "line"]
print("Original List : ", listOfStrings)
random.shuffle(listOfStrings)
print("Shuffled List : ", listOfStrings)