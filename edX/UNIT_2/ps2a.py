# Write a program to calculate the credit card balance after one year if 
# a person only pays the minimum monthly payment required by the credit 
# card company each month.

# The following variables contain values as described below:

# 1. balance - the outstanding balance on the credit card
# 2. annualInterestRate - annual interest rate as a decimal
# 3. monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. 
# At the end of 12 months, print out the remaining balance. Be sure to print 
# out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41

# instead of

# Remaining balance: 813.4141998135 

# So your program only prints out one thing: the remaining balance at the end 
# of the year in the format:

# Remaining balance: 4784.0
# A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x 
# Monthly unpaid balance)

def outstandingBalance(balance, annual_interest_rate):	
	monthly_interest_rate = annual_interest_rate / 12.0

	for month in range(12):
		minimum_monthly_payment = monthly_interest_rate * balance
		monthly_unpaid_balance = balance - minimum_monthly_payment
		updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
		balance = updated_balance_each_month

		print('Month' + str(month) + 'Remaining balance:', balance)

	return 'Remaining balance: ' + str(round(balance, 2))


<<<<<<< HEAD
print(outstandingBalance(42, 0.20, 0.04))
print(outstandingBalance(484, 0.20, 0.04))
=======




print(outstandingBalance(42, 0.20))
print(outstandingBalance(484, 0.20))
print(outstandingBalance(3329, 0.20))
>>>>>>> c0ec204829686aab43b905065aba5d6237a5dbdb
