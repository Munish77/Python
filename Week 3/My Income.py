print ("My Budget!")
# All figure monthly
income = 1000
# £2.50 coffee, 5 days per week, 4 weeks per month
coffee = 2.5 * 5 * 4
# £50 per week , 4 weeks per month
gas = 50 * 4

print(f"My income per month is £{income}")
print(f"My expenditure per month is £{coffee + gas}")
print(f"My savings per month is £{income - (coffee + gas)}")
