#Using max() and min() functions display the maximum and minimum of 5 random numbers
import random

# Generate 5 random numbers and store them in a list
numbers = [random.randint(1, 100) for _ in range(5)]

# Display the random numbers
print("Random numbers:", numbers)

# Display the maximum and minimum numbers
print("Maximum value:", max(numbers))
print("Minimum value:", min(numbers))

'''OUTPUT
Random numbers: [85, 84, 72, 36, 23]
Maximum value: 85
Minimum value: 23'''
