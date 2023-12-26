
FERRY = 500
BARQUE = 4

p = int(input())
b = int(input())
f = int(input())

sol = p - FERRY*f + BARQUE*b
if(sol <= 0):
    print(0)
else:
    print(sol)


#print(max(p - (500*f + 4*b), 0))
