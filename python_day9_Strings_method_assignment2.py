#Write a Python program to remove duplicate characters of a given string.
def remove_duplicates(input_string):
    result = []
    for word in input_string.split():
        seen = set()
        new_word = []
        for char in word:
            if char not in seen:
                seen.add(char)
                new_word.append(char)
        result.append(''.join(new_word))
    return ' '.join(result)

# Input string
input_string = "String and String Function "

# Remove duplicate characters
output_string = remove_duplicates(input_string)

print(f"Original String: {input_string}")
print(f"String after removing duplicates: {output_string}")

'''OUTPUT
String after removing duplicates: String and Functio'''


