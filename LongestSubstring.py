#Write a funtion that takes a string argument str and returns the longest substring
#of str in which the letters occur in alphabetical order.
#For eg: String = "abcdklengjwerstu". The function should return "abcd"

str1 = input("Enter any string: ")
subStr = ''
temp = ''

for i in range(len(str1)):
    temp += str1[i]
    if len(temp) > len(subStr):
        subStr = temp
    if i > len(str1)-2:
        break
    if str1[i] > str1[i+1]:
        temp = ''

print("Longest substring in alphabetical order is: " + subStr)
output  = "Longest substring in alphabetical order is: " + subStr 
f = open("output.txt", "a")
f.write("Question 2\n")
f.write(output)
f.write("\n")
f.close()