### SAVING W/ A RAISE ###

annual_salary = int(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

number_of_months = 0
current_savings = 0
portion_down_payment = 0.25
monthly_salary = annual_salary / 12
monthly_savings = monthly_salary * portion_saved
annual_return = 0.04

while current_savings < total_cost * portion_down_payment:
    # increment to the current month
    number_of_months += 1
    
    # update current savings
    current_savings += current_savings * (annual_return/12)
    current_savings += monthly_savings

    # every 6 months, increase 'annual_salary' by the 'semi_annual_raise' amount,
    # and update the relevant variables
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved

print("Number of months: ", number_of_months)