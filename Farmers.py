# Get input from the user
number_of_cows = int(input("Enter the number of cows: "))
milk_per_cow = float(input("Enter average milk produced per cow per day (litres): "))
cost_per_litre = float(input("Enter cost of production per litre (Ksh): "))

# Calculate total milk produced per day
total_milk = number_of_cows * milk_per_cow

# Calculate total cost of milk production per day
total_cost = total_milk * cost_per_litre

# Display the results
print("Number of cows:", number_of_cows)
print("Milk produced per cow:", milk_per_cow, "litres")
print("Cost per litre: Ksh", cost_per_litre)
print("Total milk produced per day:", total_milk, "litres")
print("Total cost of production per day: Ksh", total_cost)

