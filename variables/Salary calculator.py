"""Salary Breakdown
Write a program that:
Takes basic salary
Calculates:
hra = 20% of basic
da = 10% of basic
Calculates:
total_salary = basic + hra + da
Prints all values clearly"""

#code
Basic_salary = float(input("enter your basic salary"))
HRA = Basic_salary*0.2
DA = Basic_salary*0.1
Total_salary = Basic_salary+HRA+DA
print("Basic = ",Basic_salary,"\nHRA =",HRA,"\nDA =",DA,"\nTotal =",Total_salary)
