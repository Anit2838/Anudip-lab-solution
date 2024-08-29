#Write a python program to check whether a number is palindrome or not?
# Input a number from the user
num = int(input("Enter a value: "))  

# Store the original number in temp for later comparison
temp = num  

# Initialize rev to build the reversed number
rev = 0  

# Loop to reverse the number
while num > 0:  
    # Extract the last digit of num
    dig = num % 10  
    
    # Build the reversed number
    rev = rev * 10 + dig  
    
    # Remove the last digit from num
    num = num // 10  

# Compare the original number with the reversed number
if temp == rev:  
    # If they are equal, it's a palindrome
    print("This value is a palindrome number!")  
else:  
    # If not equal, it's not a palindrome
    print("This value is not a palindrome number!")

'''OUTPUT
Enter a value: 1234
This value is not a palindrome number!

Enter a value: 1221
This value is a palindrome number!'''
