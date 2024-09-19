# bisection search: find the best rate of savings to achieve a down payment on a $1M house in 36 months

def best_savings_rate(annual_salary):
	"""
	annual_salary: annual salary

	return: find the best savings rate (i.e. 'portion_saved') to achieve a down payment on a $1M house in 36 months.

	note: since hitting the 'portion_saved' exactly is a challenge, we simply want your savings
	to be within $100 of the required down payment.

	This means we can search for an integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage (using float division) to use when we are calculating the current_savings after 36 months
	"""

	semi_annual_raise = 0.07
	annual_return = 0.04
	portion_down_payment = 0.25
	total_cost = 1000000
	current_savings = 0	
	monthly_salary = annual_salary / 12
	months = 1
	down_payment = total_cost * portion_down_payment


	epsilon = 100
	bisection_steps = 0
	
	# initial 'portion saved' low estimate
	low = 0

	# initial 'portion saved' high estimate
	high = 10000

	# initial bisection search guess
	portion_saved = (low + high) // 2


	# "we simply want your savings to be within $100 of the required down payment"
	while (down_payment - current_savings) > epsilon:

		# increase current savings by the fraction of your monthly salary designated
		# for the down payment, with the currently designated portion_saved amount
		current_savings += monthly_salary * (portion_saved / 10000)

		# increase current savings by your monthly return on investments
		current_savings += current_savings * (annual_return / 12)
		
		# increment the number of months
		months += 1

		# semi-annual raise (recall, we start at month 1)
		if months % 6 == 0:
			annual_salary = annual_salary * (1 + semi_annual_raise)

			# update your monthly salary
			monthly_salary = annual_salary / 12

	return months

	



print(best_savings_rate(150000))
# print(best_savings_rate(300000))
# print(best_savings_rate(10000))