def outstandingBalance(balance, annual_interest_rate, monthly_payment_rate):	
	# preprocessing
	monthly_interest_rate = annual_interest_rate / 12.0


	for month in range(1, 13):

		minimum_monthly_payment = monthly_payment_rate * balance

		monthly_unpaid_balance = balance - minimum_monthly_payment

		updated_balance_each_month = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)

		balance = updated_balance_each_month

		# print('Month' + str(month) + 'Remaining balance:', balance)


	return 'Remaining balance: ' + str(round(balance, 2))


	



print(outstandingBalance(42, 0.20, 0.04))
print(outstandingBalance(484, 0.20, 0.04))