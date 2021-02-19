def maghsoom(a):
    b = a
    c = 0
    while b != 0:
        if a % b == 0:
            c += 1
        b -= 1
    return c
e = []
for i in range(0,20):
    d = input()
    e.append(d)
e.sort(reverse=True , key=maghsoom)
print(e)
print(e[0])
print(maghsoom(e[0]))
