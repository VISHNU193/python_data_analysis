
import random as r

myList = [r.randint(0,100) for _  in range(10)]
tup = tuple(myList)

def findK(t,k):
    tup = list(t)
    max_k = []
    min_k = []
    for i in range(k):
        max_ele = max(tup)
        max_k.append(max_ele)
        tup.remove(max_ele)

        min_ele = min(tup)
        min_k.append(min_ele)
        tup.remove(min_ele)

    print(tuple(max_k))
    print(tuple(min_k))

print(tup)
findK(tup,3)

