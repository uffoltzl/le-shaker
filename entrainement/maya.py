
n = int(input())
liste = sorted(input().split(), key=int)
j = 0
mini = int(liste[2])-int(liste[0])

for i in range(1, n-2):
    new = int(liste[i+2])-int(liste[i])
    if(new < mini):
        j = i
        mini = new

print(liste[j], liste[j+1], liste[j+2])

# mettre une condition supplémentaire de first


#N = int(input())
#tab = [int(i) for i in input().split()]
#tab.sort()

#a,b,c = 0,0,0
#mini = -1
#first = True
#for i in range(N-2):
#    if first or tab[i+2]-tab[i] < mini:
#        first = False
#        a,b,c = tab[i],tab[i+1],tab[i+2]
#        mini = tab[i+2]-tab[i]

#print(str(a)+" "+str(b)+" "+str(c))
