# bisection search: find the best rate of savings to achieve a down payment on a $1M house in 36 months

def best_savings_rate(annual_salary):

	semi_annual_raise = 0.07
	annual_return = 0.04
	portion_down_payment = 0.25
	total_cost = 1000000

	current_savings = 0

	monthly_salary = annual_salary / 12
	months = 1

	epsilon = 100
	bisection_steps = 0

	# BISECTION SEARCH TO FIND THE BEST SAVINGS RATE
	low = 0
	high = 10000

	while months <= 36:
		while current_savings - total_cost * portion_down_payment > epsilon:
			break
		break







print(best_savings_rate(150000))
print(best_savings_rate(300000))
print(best_savings_rate(10000))