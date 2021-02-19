def aval(a):  
    b = a - 1
    while b != 1:
        if a % b == 0:
            return('not prime')
            break
        else:
            b = b - 1
    else:
        return('prime')

c = 10000000
while aval(c) != 'prime':
    c = c - 1
print(c)