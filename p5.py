words ={
        "benevolent":"kind",
        "harsh":"rough",
        "generous":"kind",
        "ask":"quetsion",
        "inquire":"question"
}

print(words["generous"])


def findMeaning():
    word = input("Enter word")
    if word in words:
        print(words[word])
    else:
        print(word," is not present")

def findWords():
    meaning = input("Enter meaning")
    sameMeaning = []
    for w in words:
        if words[w] == meaning:
            sameMeaning.append(w)

    print(sameMeaning)

def addEntry():
    word = input("Enter word")
    meaning = input(f"Enter meaning of {word}")
    words[word] = meaning

def removeEntry():
    word = input("Enter word to be removed")
    del words[word]
    print(f"{word} was removed from words")

def display():
    sorted_words = dict(sorted(words.items()))
    print(sorted_words)

#print("Enter input 1.find meaning  2.find words with same meaning  3.remove an entry  4.display in sorted order  5.exit")

while True:
    print("Enter input 1.Find meaning  2.Find words with same meaning  3.Add an entry  4.Remove an entry  5.Display in sorted order  ")
    ch = int(input("Enter choice"))
    if ch == 1:
        findMeaning()
    elif ch == 2:
        findWords()
    elif ch == 3:
        addEntry()
    elif ch == 4 :
        removeEntry()
    elif ch == 5:
        display()
