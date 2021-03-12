from operator import itemgetter
natije = {}
n = str(input())
natije [("Iran","Spain")] = (n.split("-")[0] , n.split("-")[1])
n = str(input())
natije [("Iran","Portugal")] = (n.split("-")[0] , n.split("-")[1])
n = str(input())
natije [("Iran","Morocco")] = (n.split("-")[0] , n.split("-")[1])
n = str(input())
natije [("Spain","Portugal")] = (n.split("-")[0] , n.split("-")[1])
n = str(input())
natije [("Spain","Morocco")] = (n.split("-")[0] , n.split("-")[1])
n = str(input())
natije [("Portugal","Morocco")] = (n.split("-")[0] , n.split("-")[1])
#print (natije)
i = str()
j = str()
def natj (team):
    goal_difference,wins,draws,loses,points=0,0,0,0,0
    for x in natije:
        for i in range(0,2):
            if x[i] == team:
                n = int(natije[x][i])-int(natije[x][abs(i-1)])
                if n == 0:
                    draws += 1
                    points += 1
                if n > 0:
                    wins += 1
                    points += 3
                if n < 0:
                    loses += 1
                goal_difference += n
    #return {"name":team , "wins":wins , "lose":loses , "draws":draws, "goal_difference":goal_difference , "points":points}
    return [team , wins , loses , draws, goal_difference , points]

kol = [natj("Iran") , natj("Spain") , natj("Morocco") , natj("Portugal")]
kol2 = sorted(kol , key=itemgetter(5,1,0))

for t in kol2:
    print (str(t[0]) + "  wins:"+str(t[1]) + " , loses:"+str(t[2]) + " , draws:"+str(t[3]) + " , goal difference:"+str(t[4]) + " , points:"+str(t[5]))