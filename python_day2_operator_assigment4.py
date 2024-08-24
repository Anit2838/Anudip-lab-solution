# Import the math module to use the sqrt (square root) function
import math 

# Input: Lengths of the sides of the triangle
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))  
c = float(input("Enter side c: "))

# Calculate the semi-perimeter of the triangle
s = (a + b + c) / 2 

# Calculate the area using Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Apply Heron's formula to find the area
print(f"Area of the triangle: {area:.2f}")
#Print the result formatted to 2 decimal places

'''OUTPUT
Enter side a: 4
Enter side b: 5
Enter side c: 7
Area of the triangle: 9.80'''
