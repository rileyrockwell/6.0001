"""
You'll notice that in Problem 2, your monthly payment had to be a multiple of $10. Why did we make it that way? You can try running your code locally so that the payment can be any dollar and cent amount (in other words, the monthly payment is a multiple of $0.01). Does your code still work? It should, but you may notice that your code runs more slowly, especially in cases with very large balances and interest rates. (Note: when your code is running on our servers, there are limits on the amount of computing time each submission is allowed, so your observations from running this experiment on the grading system might be limited to an error message complaining about too much time taken.)

Well then, how can we calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code? We can make this program run faster using a technique introduced in lecture - bisection search!

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. One-twelfth of the original balance is a good lower bound.

What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

In short:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). Produce the same return value as you did in Problem 2.
"""

# FOR TESTING
# Initialize variables
balance = 5000  # Example balance, you can change it
annualInterestRate = 0.18  # Example annual interest rate (18%)


# Calculate monthly interest rate
monthlyInterestRate = annualInterestRate / 12.0

# Set the lower bound to the balance divided by 12 (no interest scenario)
lowerBound = balance / 12

# Set the upper bound to the balance if it accumulates maximum interest
upperBound = (balance * (1 + monthlyInterestRate)**12) / 12.0

# Set an epsilon value to define the precision of the answer (within 0.01)
epsilon = 0.01

# Save the original balance
initialBalance = balance

# Bisection search for the smallest fixed monthly payment
while upperBound - lowerBound > epsilon:
    # Calculate the midpoint between upper and lower bounds
    fixedMonthlyPayment = (upperBound + lowerBound) / 2.0
    
    # Reset the balance to the original value at the start of each iteration
    balance = initialBalance
    
    # Simulate paying off the balance over 12 months
    for month in range(12):
        # Calculate the monthly unpaid balance
        monthlyUnpaidBalance = balance - fixedMonthlyPayment
        
        # Update the balance with interest
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    # Check if the balance is paid off within 12 months
    if balance > 0:
        # If balance is still positive, increase the lower bound
        lowerBound = fixedMonthlyPayment
    else:
        # If balance is negative or zero, decrease the upper bound
        upperBound = fixedMonthlyPayment

# Print the final result rounded to two decimal places
print(f"Lowest Payment: {fixedMonthlyPayment:.2f}")
