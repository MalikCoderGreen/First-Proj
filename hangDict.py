
# Read in words from txt file (1000 words). 
words_file = open("words.txt", "r")


words = {}
key = 0
for word in words_file:
    word = word.rstrip()
    words[key] = word
    key += 1



