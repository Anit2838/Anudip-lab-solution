#Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.
# Define the div() function that takes two parameters a and b
def div(a, b):
    try:
        # Perform the division and store the result
        result = a / b
        # Print the result of the division
        print(f"The division of {a} by {b} is: {result}")
    except ZeroDivisionError:
        # Handle the case where division by zero is attempted
        print("Error: Division by zero is not allowed.")

# Call the div() function with two numbers as arguments
div(10, 2)

'''OUTPUT
The division of 10 by 2 is: 5.0'''
