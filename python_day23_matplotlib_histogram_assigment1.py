import matplotlib.pyplot as plt

# Data for the chart
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color='skyblue')

# Add labels and title
plt.xlabel('Spending Categories')
plt.ylabel('Monthly Expenses (in $)')
plt.title('Monthly Expenses Breakdown by Category')
plt.show()
