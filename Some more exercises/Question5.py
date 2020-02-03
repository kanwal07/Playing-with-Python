#question5

#pseudo- input two strings and the index, 
#traverse through the first string till i reach the index and match the other string, 
#if match then true else false

def substring(s1,s2,k):
    if((s1.index(s2,k)) == k):
        print ("True")
    else:
        print("False")

s1 = input("Enter a string: ")
s2 = input("Enter the substring: ")
index = int(input("Enter the index of the substring: "))

substring(s1,s2,index)

# index()- takes up 3 arguments
# index(substring,start position, optional end position)
# match the substring with index as the start position and return true/false