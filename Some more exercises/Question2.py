#question2
#Write a program spring.py that takes two integers m and d from the command line 
# and writes True if day d of month m is between March 21 and June 20, and False otherwise.

#pseudo- 1.take input day and month-- 2. check the month between 3,4,5,6 -- 3. check the date between required numbers-- 4. print result 

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))



if(month == 3 or month == 4 or month == 5 or month == 6):
    if(month == 3): #march
        if(day >=21 and day <=31):
            print("True")
    elif(month == 4 ): #april
        if(day == 31):
            print("False")
    elif(month == 5): #may
        if(day >=1 and day <=31):
            print("True")    
    elif(month == 6): #june
        if(day >=1 and day <=20):
            print("True")
    else:
        print("False")
else:
    print("False")