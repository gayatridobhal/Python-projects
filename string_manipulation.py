with open("story.txt", "r") as file:
    content = file.read()
#print content
    print(content)
#convert to lowercase
    str_lower = content.lower()
#remove punctuation
    str_new = str_lower.replace(",","").replace(".","").replace("!","").replace("'","").replace(":","").replace(";","")
#split text into a list of words
    words = []
    word = ""
    n = 0
    for letter in str_new:
        if letter != " ":
            word = word + letter
        else:
            words.append(word)
            word = ""
    print(words)
print("\n")
#count frequency of each word
dictt = {}
for word in words:
    dictt[word] = words.count(word)
print(dictt)
print("\n")
#print the 5 most common words and their counts
dict_sort = dict(sorted(dictt.items(), key=lambda item: item[1], reverse=True))
print(list(dict_sort.items())[:5])