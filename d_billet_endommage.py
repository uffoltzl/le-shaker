
L, C = map(int, input().split())
ligne = [0 for _ in range(L)]
col = [0 for _ in range(C)]
mat = []

for l in range(L):
    line = input()
    mat.append(line)
    for c in range(C):
        if(line[c] == '-'):
            ligne[l] += 1
            col[c] += 1

nb_l = [int(i) for i in input().split()]
nb_c = [int(i) for i in input().split()]

print(col)
