
M = int(input())
R = [int(i) for i in input().split()]
N = int(input())
A = sorted([int(i) for i in input().split()])

j = 0
res = "POSSIBLE"
for i in range(M):
    if(j >= N):
        break
    if(A[j] <= i):
        res = "IMPOSSIBLE"
        break
    else:
        j += R[i]

if(j < N):
    res = "IMPOSSIBLE"

print(res)
