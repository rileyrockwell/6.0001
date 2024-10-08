# w/ a raise

def number_of_months(annual_salary, portion_saved, total_cost, semi_annual_raise):
	portion_down_payment = 0.25
	current_savings = 0
	annual_return = 0.04

	monthly_salary = annual_salary / 12
	months = 1

	# while current savings is less than the down payment amount (on a monthly basis)
	while current_savings < portion_down_payment * total_cost:

		# increase current savings by the fraction of your monthly salary designated for the down payment
		current_savings += monthly_salary * portion_saved

		# increase current savings by your monthly return on investments
		current_savings += current_savings * (annual_return / 12)
		
		# increment the number of months
		months += 1

		# SEMI-ANNUAL RAISE
		# (recall, we start at month 1)
		if months % 6 == 0:
			annual_salary = annual_salary * (1 + semi_annual_raise)

			# update your monthly salary
			monthly_salary = annual_salary / 12


	return "Number of months: " + str(months)


print(number_of_months(120000, 0.05, 500000, 0.03))
print(number_of_months(80000, 0.10, 800000, 0.03))