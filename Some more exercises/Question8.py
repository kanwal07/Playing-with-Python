#question8
#Write a function flatten that returns a simple list containing all the values in a nested list. 
# For example, flatten([2,9,[2,1,13,2],8,[2,6]]) returns [2,9,2,1,13,2,8,2,6]



def flatten(somelist):
    
    newList = []

    for element in somelist:
        if(type(element)==int):
            newList.append(element)
        else:
            newList.extend(element)

    print(newList)

nestedList = [2,9,[2,1,13,2],8,[2,6]]
flatten(nestedList)
