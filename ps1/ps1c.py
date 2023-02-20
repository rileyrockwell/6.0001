### BEST SAVINGS RATE, INCORPORATING BISECTION SEARCH ###

# Collaborator: Alan Hussey

# User input
user_annual_salary = 150000
user_monthly_salary = user_annual_salary / 12
user_annual_return = 0.04
user_semi_annual_raise = 0.07
user_total_cost = 1000000
user_down_payment = user_total_cost * 0.25

# Bisection search initialization
high = 1.0
low = 0
guess = (high + low)/2.0
bisection_steps = 0
number_of_months = 0

while number_of_months != 36:
    annual_salary = user_annual_salary
    monthly_salary = user_monthly_salary
    annual_return = user_annual_return
    semi_annual_raise = user_semi_annual_raise
    total_cost = user_total_cost
    down_payment = user_down_payment

    portion_saved = guess
    number_of_months = 0
    current_savings = 0
    monthly_savings = monthly_salary * portion_saved

    while current_savings < down_payment:
        # increment to the current month
        number_of_months += 1

        # update current savings
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_savings

        # every 6 months, increase 'annual_salary' by the 'semi_annual_raise' amount,
        # and update the relevant variables
        if number_of_months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
            monthly_salary = annual_salary / 12
            monthly_savings = monthly_salary * portion_saved

    print(number_of_months, low, high, guess)
    if number_of_months >= 36:
        low = guess
    else:
        high = guess
    guess = (high + low) / 2.0
    bisection_steps += 1
    if bisection_steps > 5:
        break


print("Number of months:", number_of_months)
print("Bisection steps:", bisection_steps)