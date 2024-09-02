#Write a Python program to remove a newline in
string = "\nBest \nDeeptech \nPython \nTraining\n"

print("Original string with newlines:")
print(string)

# Remove all newline characters
string_without_newlines = string.replace("\n", "")

print("\nString after removing newlines:")
print(string_without_newlines)

'''OUTPUT
Original string with newlines:

Best 
Deeptech 
Python 
Training


String after removing newlines:
Best Deeptech Python Training'''
