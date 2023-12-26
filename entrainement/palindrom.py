def palindrom(chaine):
    return chaine == chaine[::-1]

#print(palindrom("ABBA"))
#print(palindrom("KAYAK"))
#print(palindrom("ABCA"))

def dist(elem):
    return elem[1]-elem[0]

def part_palindrom(chaine):
    palin = []
    for i in range(len(chaine)):
        for j in range(i+1, len(chaine)+1):
            if(palindrom(chaine[i:j])):
                palin.append((i, j))
    palin.sort(key=dist, reverse=True)
    return chaine[palin[0][0]:palin[0][1]]

print(part_palindrom("ABBA"))
print(part_palindrom("CABBA"))
print(part_palindrom("ABBAC"))
print(part_palindrom("ABABBAAB"))
