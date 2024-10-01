import matplotlib.pyplot as plt

# Input data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

# Create a pie chart
plt.figure(figsize=(8, 6))
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=90, colors=['#66b3ff','#99ff99','#ff9999','#ffcc99','#c2c2f0'])
plt.title('Monthly Income Distribution by Source')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
