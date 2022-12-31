from operator import itemgetter
n = int(input())
javab = []
kol = []

for i in range(0,n):
    javab = input().split(".")
    kol.append(javab)

new_kol = []
for item in kol:
    cap = item[1].capitalize()
    new_kol.append([item[0] , str(cap) , item[2]])
new_kol.sort()
new_kol.sort(key=itemgetter(1))
new_kol.sort(key=itemgetter(0))
for item in new_kol:
    print(str(item[0]) + " " + str(item[1]) + " " + str(item[2]))