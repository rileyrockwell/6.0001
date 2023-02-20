semi_annual_raise = 0.07
current_savings = 0
annual_salary = 150000


def bisection_search(high, low, guess_is_incorrect, guess_is_too_low):
    guess = (high + low) / 2.0
    bisection_steps = 0    
    while guess_is_incorrect(guess):
        if guess_is_too_low(guess):
            low = guess
        else
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
    current_savings += current_savings * (annual_return/12)
    current_savings += monthly_savings

    # every 6 months, increase 'annual_salary' by the 'semi_annual_raise' amount,
    # and update the relevant variables
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * savings_rate
        current_savings_after_nth_month = monthly_savings

print(bisection_search(10, 0, ..., ...)


### ORIGINAL CODE FROM PS3C.PY ###

annual_salary = 150000
semi_annual_raise = 0.07
annual_return = 0.04
portion_down_payment = 0.25
total_cost = 10**6
current_savings = 0
epsilon = 100
monthly_salary = annual_salary / 12
number_of_months = 36
low = 0
high = 1.0
guess = (high + low)/2.0


# determine the best savings rate, given t = 36 months
while ['function including the rate'] - ['correct answer'] >= epsilon:
while total_cost * portion_down_payment - current_savings >= epsilon:
    best_savings_rate = (high + low)/2.0


    while current_savings < total_cost * portion_down_payment:
    # increment to the current month
    number_of_months = 36
    
    # update current savings
    current_savings += current_savings * (annual_return/12)
    current_savings += monthly_savings

    # every 6 months, increase 'annual_salary' by the 'semi_annual_raise' amount,
    # and update the relevant variables
    if number_of_months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved



# incorporate semi-annual raise and returns on investments

current_savings_after_36_months = 0
t = 0
annual_salary = 150000
monthly_salary = annual_salary / 12
low = 0.0
high = 1.0
guess = (high + low)/2.0
epsilon = 100
down_payment = 250000
bisection_steps = 0

for month in range(0, 36):
    if 



for months in range(0, 36):
    
    # update current savings
    current_savings += current_savings * (annual_return/12)
    current_savings += monthly_savings

    # every 6 months, increase 'annual_salary' by the 'semi_annual_raise' amount,
    # and update the relevant variables
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * [something]

        current_savings_after_nth_month = monthly_savings

# how much do you need for the down payment?
while down_payment - current_savings_after_nth_month >= epsilon:
    if [condition 1]:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    bisection_steps += 1
    
    t = 0
    current_savings_after_36_months = 0

    while t <= 36:
        current_savings_after_36_months += monthly_salary * guess
        t += 1

print(guess)
print(bisection_steps)

print(current_savings_after_36_months)

if is_word_guessed(secret_word, letters_guessed) == False:
    print("--------")
    print("You have", str(n - number_of_guesses), "guesses left.")
    print("Available letters:", ''.join(get_available_letters(letters_guessed)))

    # get user input
    user_guess = str(input("Please guess a letter: ").lower())

    boolean1 = user_guess.isalpha()

    if boolean1 == False:
        warnings -= 1
        print("Oops! That is not a valid letter. You have", str(warnings), "warnings left:",
              get_guessed_word(secret_word, letters_guessed))
        if warnings == 0:
            number_of_guesses += 1
            warnings = 3
    else:
        letters_guessed.append(user_guess)

        if letters_guessed[-1] in secret_word:
            print("Good guess:", get_guessed_word(secret_word, letters_guessed))
        else:
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            number_of_guesses += 1
else:
    print("Congratulations, you guessed the secret word:", secret_word)
    break
