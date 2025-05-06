str1 = "Hello we are learning python program"
# output = [('hello',5), ('we',2), ('are',3), ('learning', 8), ('python',6), ('program',7)]

output = []

wordlist = str1.split(" ")
for word in wordlist:
    word_len = len(word)
    result = [word, word_len]
    tup1 = tuple(result)
    output.append(tup1)

print(output)
