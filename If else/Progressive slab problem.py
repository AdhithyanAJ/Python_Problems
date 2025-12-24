#if else problem 3
#Progressive slab problems
annual_income = int(input("Enter your annual income:"))
if(annual_income<0):
    print("Invalid income")
elif(annual_income <=250000):
    print("No tax")
elif( annual_income<=500000):
    print("Tax = ",((annual_income-250000)*5)/100) 
elif( annual_income<=1000000):
    print("Tax = ",(((250000*5)/100)+(((annual_income-500000)*20)/100)))
else:
    print("Tax = ",((250000*5)/100)+((500000*20)/100)+(((annual_income-1000000)*30)/100))

