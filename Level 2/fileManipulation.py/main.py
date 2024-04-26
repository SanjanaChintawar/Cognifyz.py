word_count = {}

with open("data.txt", mode="r") as file:
    number_of_words = 0

    for line in file:
        words = line.split()
        number_of_words += len(words)
        for word in words:
            word = word.strip().lower().strip(".,_?!")
            if word:
                word_count[word] = word_count.get(word, 0) + 1

sorted_word_counts = sorted(word_count.items())
for word, count in sorted_word_counts:
    print(f'{word}: {count}')

