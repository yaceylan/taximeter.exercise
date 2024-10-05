start_price = 4.8
km = int(input("Please enter a number: "))
if km > 5:
    costs = 1.9
else:
    costs = 2.1
total_expenses = start_price + costs * km
print ("Your costs are:", total_expenses)
