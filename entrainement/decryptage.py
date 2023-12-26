
mot = input()
n = int(input())
dict = [input() for _ in range(n)]

sol = []

for i in range(n):
    if(dict[i][0] == mot[0] and dict[i][-1] == mot[-1] and len(dict[i]) == len(mot)):
        mot2 = dict[i][1:len(mot)-1]
        cond = True
        for j in range(i, len(mot)-1):
            if(mot[j] in mot2):
                mot2.remove(mot[j])
            else:
                cond = False
                break
        if(cond):
            sol.append(dict[i])

sol.sort()
for i in range(len(sol)):
    print(sol[i])


#M = input()
#Msorted = ''.join(sorted(M))
#N = int(input())

#listValidWord = []
#for i in range(N) :
#	m = input()
#	if(m[0] == M[0] and m[len(m) - 1] == M[len(M) - 1] and ''.join(sorted(m)) == Msorted) :
#		listValidWord.append(m)

#listValidWord.sort()
#print(*listValidWord, sep="\n")
