#Progressive slab problems
"""Takes annual income as input
Calculates tax based on slabs:
Income (₹)	Tax
Up to 2,50,000 = No tax
2,50,001 - 5,00,000	= 5%
5,00,001 - 10,00,000 = 20%
Above 10,00,000 = 30%

Print:
"No tax"
OR "Tax = ₹<amount>" """

#code
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

