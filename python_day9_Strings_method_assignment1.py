#Write a Python program to Count all letters, digits, and special symbols from the given string
def count_elements(string):
    letters = 0
    digits = 0
    special_symbols = 0

    for char in string:
        if char.isalpha():
            letters += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1

    return letters, digits, special_symbols

# Input string
string = "P@#yn26at^&i5ve"

# Count letters, digits, and special symbols
letters, digits, special_symbols = count_elements(string)

print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special Symbols: {special_symbols}")

'''OUTPUT
Letters: 8
Digits: 3
Special Symbols: 4'''
