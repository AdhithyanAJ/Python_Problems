#variables problem 3
"""Write a program that:
Takes total seconds as input
Converts it into:
Hours
Minutes
Seconds"""

#code
time = int(input("enter time in seconds"))
hour = time//3600
minutes = (time-(hour*3600))//60
seconds = (time-(hour*3600))-(minutes*60) #seconds = time % 60 we can use it for shortcut 

print("hour =",hour)
print("minutes =",minutes)
print("seconds=",seconds)



