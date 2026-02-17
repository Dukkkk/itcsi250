sentence = "the cat and the dog and the bird the"
words = sentence.split()
counts = {}

for i in words:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
for word in counts:
    if counts[word] > 1:
        print(word , ":", counts[word])