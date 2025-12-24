# take an input and print the conditions as below 
"""Takes an integer n
If n is:
Positive and even → print "Positive Even"
Positive and odd → print "Positive Odd"
Negative → print "Negative"
Zero → print "Zero" """

#code
number = int(input("enter your number:"))
if(number>0 and number%3==0 and number%5==0):
    print("Fizzbuzz")
elif(number>0 and number%2 ==0):
    print("Positive even!")
elif(number>0 and number%2!=0):
    print("Positive odd!")
elif(number<0):
    print("Negative!")
else:
    print("Zero!")    