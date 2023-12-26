
N = int(input())
P1 = int(input())
P2 = int(input())
P3 = int(input())

res = 0
if(N <= 100):
    res += N*P1
else:
    res += 100*P1
    if(N <= 200):
        res += (N-100)*P2
    else:
        res += 100*P2+(N-200)*P3

print(res)
