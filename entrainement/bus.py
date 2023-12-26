def calcul_bus(N, P):
    return N//P + int(N%P != 0)

print(calcul_bus(20, 10))
print(calcul_bus(21, 10))

#nbPerson = int(input())
#nbSeat = int(input())

#print(math.ceil(nbPerson / nbSeat))
