#Write a python program finding the factorial of a given number using a while loop
# Input a number from the user
number = int(input("Enter a number: "))

# Initialize the factorial result to 1
factorial = 1

# Initialize a counter variable
i = 1

# Use a while loop to calculate the factorial
while i <= number:
    factorial *= i  # Multiply factorial by the current counter value
    i += 1  # Increment the counter

# Print the result
print(f"The factorial of {number} is {factorial}.")

'''OUTPUT
Enter a number: 5
The factorial of 5 is 120'''
