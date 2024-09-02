#Write a Python program to count the occurrences of each word in a given sentence
# Input string
string= "To change the overall look of your document. To change the look available in the gallery"

# Convert the sentence to lowercase and split it into words
words = string.lower().split()

# Create an empty dictionary to store the word counts
word_count = {}

# Count the occurrences of each word
for word in words:
    # Remove any punctuation from the word
    word = word.strip(".")
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word count
for word, count in word_count.items():
    print(f"{word}: {count}")

'''OUTPUT
to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1'''

