### USING FUNCTIONS ###

def bisection_search(high, low, guess_is_incorrect, guess_is_too_low):
    guess = (high + low) / 2.0
    bisection_steps = 0
    while guess_is_incorrect(guess):
        # try using the guess
        if guess_is_too_low(guess):
            low = guess
        else:
            high = guess
        guess = (high + low) / 2.0
        bisection_steps += 1

    return guess


# guess_is_incorrect: return Boolean
# guess_is_too_low: return Boolean

def will_reach_savings_goal_in_exactly_36_months(guess):
    savings_rate = guess

    for months in range(0, 36):
        # update current savings
        current_savings += current_savings * (annual_return / 12)
        current_savings += monthly_savings

    # every 6 months, increase 'annual_salary' by the 'semi_annual_raise' amount,
    # and update the relevant variables
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * savings_rate
        current_savings_after_nth_month = monthly_savings


print(bisection_search(10, 0, 100, 100))