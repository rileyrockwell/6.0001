annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))

number_of_months = 0
current_savings = 0
portion_down_payment = 0.25
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
annual_return = 0.04

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * (annual_return/12)
    current_savings += monthly_savings
    number_of_months += 1

print("Number of months: ", number_of_months)