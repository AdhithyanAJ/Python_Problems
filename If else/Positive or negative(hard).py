#if else problem 1
# take an input and print the conditions as below 

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