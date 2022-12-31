from operator import itemgetter
n = int(input())
javab = []
kol = []
genres = {"Horror":0, "Romance":0, "Comedy":0, "History":0 , "Adventure":0 , "Action":0}
for i in range(0,n):
    javab = input().split(" ")
    kol = kol + [javab[1] , javab[2] , javab[3]]
counts = {i:kol.count(i) for i in kol}
genres.update(counts)
list=[]
for key in genres:
    item = [key , genres[key]]
    list.append(item)

list.sort(key=itemgetter(0))
list.sort(reverse=True , key=itemgetter(1))
for item in list:
    print(str(item[0]) + " : " + str(item[1]))