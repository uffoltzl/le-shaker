
N, E = map(int, input().split())
voisin = [0 for _ in range(N)]

for _ in range(E):
    a, b = map(int, input().split())
    voisin[a-1] += 1
    voisin[b-1] += 1

print(min(voisin))
