
def findFreq(char,string):
    c = 0
    for x in string:
        if x == char:
            c += 1
    return c

def char_freq(string):
    freq ={}
    for x in string:
        freq[x] = findFreq(x,string)

    print(freq)

char_freq("hello world")

