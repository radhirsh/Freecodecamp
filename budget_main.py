# Import the budget module and create_spend_chart function
import budget
from budget import create_spend_chart

# Create a "Food" category and perform transactions
food = budget.Category("Food")
food.deposit(1000, "Initial deposit")
food.withdraw(10.15, "Groceries")
food.withdraw(15.89, "Restaurant and more food for dessert")

# Print the current balance of the "Food" category
print("Food category balance:", food.get_balance())

# Create a "Clothing" category and perform transactions
clothing = budget.Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

# Print the details of the "Food" and "Clothing" categories
print("Food category details:\n", food)
print("Clothing category details:\n", clothing)

# Generate and print the spend chart for the given categories
print("Spend chart:\n", create_spend_chart([food, clothing]))

# Run the unit tests automatically
main(module='test_module', exit=False)
