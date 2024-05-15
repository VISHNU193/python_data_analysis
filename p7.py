import random as r

st = int(input("Enter start"))
end = int(input("Enter end"))
even_random = [r.randrange(st,end,2) for _ in range(10)]

print(even_random)

def getRandom(string):
    l = len(string)
    idx = r.randint(0,l-1)
    return string[idx]

print(getRandom("vishnu"))

def generateUnique(start,end,number):
    res =[]
    for i in range(number):
        num = r.randint(start,end)
        
        while num in res:
            num = r.randint(start,end)
        res.append(num)

    print(res,len(res))

generateUnique(1,100,20)
