# Now write a program that calculates the minimum fixed monthly payment 
# needed in order pay off a credit card balance within 12 months. 
# By a fixed monthly payment, we mean a single number which does 
# not change each month, but instead is a constant amount that 
# will be paid each month.

# In this problem, we will not be dealing with a minimum monthly payment rate.

# The following variables contain values as described below:
# 1. balance - the outstanding balance on the credit card
# 2. annualInterestRate - annual interest rate as a decimal

# The program should print out one line: the lowest monthly payment that will 
# pay off all debt in under 1 year, for example:

# Lowest Payment: 180 

# Assume that the interest is compounded monthly according to the balance 
# at the end of the month (after the payment for that month is made). 
# The monthly payment must be a multiple of $10 and is the same for all 
# months. Notice that it is possible for the balance to become negative 
# using this payment scheme, which is okay. 
# A summary of the required math is found below:

# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x 
# Monthly unpaid balance)

def outstandingBalance(balance, annual_interest_rate):
	"""
	balance: the outstanding balance on the credit card
	annualInterestRate: annual interest rate as a decimal

	return: the lowest monthly payment that will pay off all debt in under 1 year.
	
	note:
	- assume that the interest is compounded monthly, according to the balance
	  at the end of the month (after the payment for that month is made)

	- the monthly payment must be a multiple of $10 and is the same for all months.

	- notice that it is possible for the balance to become negative using this payment
	  method, which is okay
	
	
	variables:
	- monthly interest rate = (annual interest rate) / 12.0

	- monthly unpaid balance = (previous balance) - (minimum fixed monhtly payment)

	- updated balance each month = (monthly unpaid balance) +
	  (monthly interest rate * monthly unpaid balance)

	"""
	# REVIEW
	initial_balance = balance

	# given: minimum_fixed_monthly_payment is a multiple of 10
	minimum_fixed_monthly_payment = 10

	# compute monthly_interest_rate
	monthly_interest_rate = annual_interest_rate / 12.0

	# initialize month
	month = 0

	# objective: determine the minimum_fixed_monthly_payment within 12 months
	while month < 12:
		# update the monthly_unpaid_balance for each iteration
		monthly_unpaid_balance = balance - minimum_fixed_monthly_payment

		# update the balance, assuming that the interest is compounded monthly, 
		# according to the balance at the end of the month (after the payment for that month
		# is made).

		# balance = outstanding_balance + interest on current balance
		balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

		print(balance)

		# increment month
		month += 1


	# while the balance is not paid off (i.e. > 0)
	while balance > 0:
		pass




print(outstandingBalance(1200, 0.10))