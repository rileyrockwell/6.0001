def outstandingBalance(balance, annual_interest_rate):	
	minimum_fixed_monthly_payment = 0

	monthly_interest_rate = annual_interest_rate / 12.0

	monthly_unpaid_balance = balance - minimum_fixed_monthly_payment

	monthly_updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)


	# incorporate the minimum_fixed_monthly_payment

	lowest_payment = 0

	return "Lowest Payment: ", lowest_payment



print(outstandingBalance(3329, 0.2))
print(outstandingBalance(4773, 0.2))
print(outstandingBalance(3926, 0.2))