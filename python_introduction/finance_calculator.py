monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 0.05 * 5)
print(f"Your monthly savings are ${monthly_savings}")
print(f"Projected savings after one years is, with interest, is ${projected_savings}")