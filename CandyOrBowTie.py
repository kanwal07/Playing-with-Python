#Candy or Bowtie
#Write a program that draws a candy or a bowtie, given the following user specifications:
#- candy (c) or bowtie (b)
#- width (even or odd integer)
# tight or relaxed pattern (default is tight, see first two diagrams)

def bowtie(num):
    row=num
    while row>0: 
        space = num-row
        while space>0:
            print(end=" ")
            space = space-1
        star = num-row-1
        while star<num-1:   
            print("*",end=" ")
            star = star+1
        row = row-1
        print()

##Function for traingle
def candy(num):
    row = 0
    while row<num:
        space = num-row-1
        while space>0:
            print(end=" ")
            space = space-1
        star = row+1
        while star>0:
            print("*", end=" ")
            star= star-1
        row=row+1
        print() 

a=0
num= int(input("Enter the width: "))
option= int(input("Enter 1 for bowtie, 2 for candy : "))

if option == 1:
    bowtie(num)
    candy(num)

if option == 2:
    bowtie(num)
    candy(num)
    bowtie(num)
    candy(num)

