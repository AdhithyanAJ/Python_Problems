"""Takes three integers as input: a, b, and c
Prints:
"a is the largest" if a is greatest
"b is the largest" if b is greatest
"c is the largest" if c is greatest
If all three numbers are equal, print:
"All numbers are equal" """

#code
a = int(input("enter the first number"))
b = int(input("enter the second number"))
c = int(input("enter the third number"))
if(a ==b and b==c):
    print("All number are equal")
elif(a>=b and a>=c):
    print( a,"is the largest")
elif(b>=a and b>=c):
    print(b,"is the largest")
else:
    print(c,"is the largest")