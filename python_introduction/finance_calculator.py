#User's Financial Details
monthly_income = float (input ("Enter your monthly income:"))
total_monthly_expenses = float (input("Enter your total monthly expenses:"))
#Calculate monthly savings
monthly_savings = monthly_income - total_monthly_expenses
#Calculate projected savings after one year (assume annual interest rate of 0.05)
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
#Print results
print (f"Your monthly savings are: ${monthly_savings}")
print (f"Project annual savings with 5%: ${projected_savings}")