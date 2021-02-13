import random
hads = random.randint(a=1,b=99)
print(hads)
javab = input('say me ')
javab = str(javab)
while javab != 'd':
    if javab == 'b':
        b = hads
        hads = random.randint(a,b)
    if javab == 'k':
        a = hads
        hads = random.randint(a,b)
    print(hads)
