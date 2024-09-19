base_annual_salary = 150000

#  fixed data
total_cost = 1000000         # total cost of dream house
percent_down_payment = 0.25  # 25% of total cost
monthly_r = 0.04 / 12        # monthly rate of return of investment
semi_annual_raise = 0.07     # increae in annual salary every after six months
down_payment = total_cost * percent_down_payment
months = 36                  # minimum months to pay for down payment

#  margin of error for bisection search
epsilon = 100   # within 100 pesos of the required down payment

#  bounds for bisection search
initial_high = 10000  # 10000 for 100%
high = initial_high   # high boundary for the formula (High + Low)/2
low = 0               # lower boundary

#  initial values for the while loop
current_savings = 0
step = 0   # step in bisection search
# floor division to get the integer quotient
portion_saved = (high + low) // 2

#  start of bisection search
while abs(current_savings - down_payment) > epsilon:
    #  for each iteration in for loop, all variable are reset to initial values except step variable
    step += 1
    current_savings = 0
    annual_salary = base_annual_salary
    monthly_salary = annual_salary / 12
    monthly_deposit = monthly_salary * (portion_saved / 10000)

    #  computes current savings every month for 36 months
    #  iteration start from 1 intead of 0 since 0%6 = 0
    #  and this will satisfy the condition of semi-annual increase
    for month in range(1, months + 1):
        #  increase in annual salary every 6 months.
        #  remainder of zero means that it is the 6th, 12th, 18th count and so on
        current_savings += (current_savings * monthly_r)
        current_savings += monthly_deposit
        if month % 6 == 0:
            annual_salary += (annual_salary * semi_annual_raise)
            monthly_salary = annual_salary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)

    #  assigns portion_saved to variable prev_portion_saved
    #  to be used as conditional statement to exit from the loop
    prev_portion_saved = portion_saved
    if current_savings < down_payment:
        low = portion_saved
    else:
        high = portion_saved

    #  computes new savings rate with new bounds
    #  cast to integer so that low and high bounds will converge completely
    #  if the solution is outside the search space with respect to high bound
    portion_saved = int(round((high + low) / 2))
    #  if portion_saved remains constant with comparison to prev_portion_saved, solution is outside search space
    #  break to exit from infinite loop
    if prev_portion_saved == portion_saved:
        break

print()
#  after 36 iterations, if current savings does not suffice the required down payment,
#  base annual salary is not enough for the required down payment
if portion_saved == initial_high:
    print("Not possible to acquire the house within 36 months.")
else:
    print("Best savings rate: {}".format(round(portion_saved / 10000, 4)))
    print("Steps in Bisection search: {}".format(step))


# bisection search: find the best rate of savings to achieve a down payment on a $1M house in 36 months
# collaborator: https://github.com/pauquilao/MIT-6.0001-Problem-Sets/blob/master/ps1/ps1c.py


def best_savings_rate(annual_salary, duration):
	"""
	annual_salary: annual salary

	return: find the best savings rate (i.e. 'portion_saved') to achieve a down payment on a $1M house in 36 months.

	note: since hitting the 'portion_saved' exactly is a challenge, we simply want your savings
	to be within $100 of the required down payment.

	This means we can search for an integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage (using float division) to use when we are calculating the current_savings after 36 months
	"""

	total_cost = 1000000
	portion_down_payment = 0.25
	annual_return = 0.04
	monthly_return = annual_return / 12
	semi_annual_raise = 0.07
	down_payment = total_cost * portion_down_payment
	months = duration



	# to ensure current savings can cover the downpayment (to within 100 dollars)
	epsilon = 100

	# for bisection
	low = 0
	initial_high = 10000
	high = initial_high

	# miscellaneous
	current_savings = 0
	iterations = 0
	portion_saved = (high + low) // 2

	# "we simply want your savings to be within $100 of the required down payment"
	while (down_payment - current_savings) > epsilon:

		iterations += 1
		# reintialize current savings for each iteration (b/c of the for loop)
		current_savings = 0
		# from the parameter
		annual_salary = annual_salary
		# redefine monthly salary
		monthly_salary = annual_salary / 12
		# initialize a monthly_savings variable
		monthly_savings = monthly_salary * (portion_saved / 10000)

		for month in range(duration):
			current_savings += current_savings * monthly_return
			current_savings += monthly_savings
			
			# semi-annual raise
			if month % 6 == 0:
				annual_salary += annual_salary * semi_annual_raise
				monthly_salary = annual_salary / 12
				monthly_savings = monthly_salary * (portion_saved / 10000)

		

		print(down_payment, current_savings)

		### bisection ###
		# intialize a new variable previous_portion_saved
		previous_portion_saved = portion_saved

		# intialize the lower bound of the bisection, as you will need to save more
		if current_savings < down_payment:
			low = portion_saved
		
		# initialize the upper bound of the bisection, as you will need to save less
		else:
			high = portion_saved

		# reintialize portion_saved for each iteration
		portion_saved = int(round((high + low) / 2))

		# if the bisection is complete
		if previous_portion_saved == portion_saved:
			break


	if portion_saved == initial_high:
		print("Not possible to save for the down payment in 36 months")
	else:
		print("Best savings rate: " + str(round(portion_saved / 10000, 4)))
		print("Bisection steps: " + str(iterations))




print(best_savings_rate(150000, 36))
# print(best_savings_rate(300000))
# print(best_savings_rate(10000))