"""
Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:

Lowest Payment: 180

Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Hints
Hint: How to think about this problem?

Start with $10 payments per month and calculate whether the balance will be paid off in a year this way (be sure to take into account the interest accrued each month).
If $10 monthly payments are insufficient to pay off the debt within a year, increase the monthly payment by $10 and repeat.
Hint: A way of structuring your code

If you are struggling with how to structure your code, think about the following:
Given an initial balance, what code would compute the balance at the end of the year?
Now imagine that we try our initial balance with a monthly payment of $10. If there is a balance remaining at the end of the year, how could we write code that would reset the balance to the initial balance, increase the payment by $10, and try again (using the same code!) to compute the balance at the end of the year, to see if this new payment value is large enough.
I'm still confused!

A good way to implement this problem will be to use a loop structure. You may want to refresh your understanding of while loops. Think hard about how the program will know when it has found a good minimum monthly payment value - when a good value is found, the loop can terminate.
Be careful - you don't want to overwrite the original value of balance. You'll need to save that value somehow for later reference!
"""

# Calculate monthly interest rate
monthlyInterestRate = annualInterestRate / 12.0

# Set a starting value for the fixed monthly payment
fixedMonthlyPayment = 10

# Save the original balance to reset each time we check a payment amount
initialBalance = balance

# Loop to find the minimum payment
while True:
    # Reset the balance to the original value at the beginning of each loop
    balance = initialBalance
    
    # Simulate paying off the balance over 12 months with the current fixed payment
    for month in range(12):
        # Calculate the monthly unpaid balance
        monthlyUnpaidBalance = balance - fixedMonthlyPayment
        
        # Update the balance with interest
        balance = monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance)
    
    # If the balance is paid off (or goes negative), we're done
    if balance <= 0:
        break
    
    # Otherwise, increase the fixed monthly payment by $10 and try again
    fixedMonthlyPayment += 10

# Print the result
print("Lowest Payment:", fixedMonthlyPayment)