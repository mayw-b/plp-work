# A Program to Store a list of words and create a new list with words having odd length
word_list = ["apple", "banana", "orange", "grape", "pineapple", "kiwi"]
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)