
import math

v = 100

Ya, Yb = map(float, input().split())
N, T = map(int, input().split())

def distanceTot(e1, e2):
    return math.sqrt((e1[0]-Ya)**2 + (e1[1]-Yb)**2) + math.sqrt((e2[0]-Ya)**2 + (e2[1]-Yb)**2)

sol = []
for _ in range(N):
    name = input()
    coord = [[float(e) for e in input().split()] for _ in range(T)]
    for i in range(T-1):
        if(distanceTot(coord[i], coord[i+1]) <= v):
            sol.append(name)
            break

print(' '.join(sol))

#    for j in range(T):
#        X,Y = [float(k) for k in input().split()]
#        if j>0 and (distance(lastX,lastY,Xb,Yb)+distance(Xb,Yb,X,Y)) <= vitesseMax:
#            sol.append(name)
#            break
#        lastX,lastY = X,Y
