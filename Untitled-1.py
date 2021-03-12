def fuctorial(a):
    if a==1:
        return 1
    else:
        return a*fuctorial(a-1)

print fuctorial(6)