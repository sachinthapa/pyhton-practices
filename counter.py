from collections import Counter

words = "if there was there was but if \
... there was not there was not".split()

word_count = {}

for word in words:
    if word not in word_count:
        word_count[word] = []
    word_count[word].append(word)

for key, value in word_count.items():
    print(key," = ", len([word for word in value]))    

print(Counter(words))
