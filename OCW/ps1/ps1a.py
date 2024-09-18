# w/out a raise

def number_of_months(annual_salary, portion_saved, total_cost):
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

	return "Number of months: " + str(months)


print(number_of_months(120000, 0.10, 1000000))
print(number_of_months(80000, 0.15, 500000))