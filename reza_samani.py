import operator
def maghsoom(a):
    b = a
    rp=[]
    while b != 0:
        if a%b == 0:
            rp.append(b)
        b -= 1
    return rp
dict = {}
for i in range(0,10):
    d = int(input())
    c = 0
    for x in maghsoom(d):
        if len(maghsoom(x)) == 2:
            c +=1
    dict [d] = c
inverse = [(value, key) for key, value in dict.items()]
javab = (max(inverse)[1])
print (javab , dict[javab])