#Python program to check if the given string is a palindrome 
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(s.split()).lower()
    
    # Get the length of the cleaned string
    length = len(cleaned_string)
    
    # Check if the cleaned string is the same forwards and backwards
    for i in range(length // 2):
        if cleaned_string[i] != cleaned_string[length - i - 1]:
            return False
    return True

# Get user input
string_to_check = input("Enter a string to check if it's a palindrome: ")

# Check if the string is a palindrome and print the result
if is_palindrome(string_to_check):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


'''OUTPUT
Enter a string to check if it's a palindrome: Anit
The string is not a palindrome.

Enter a string to check if it's a palindrome: ANNA
The string is a palindrome.'''
