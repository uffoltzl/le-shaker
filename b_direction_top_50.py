
nom = input()
voyelles = ['a', 'e', 'i', 'o', 'u', 'y']

def palindrom(chaine):
    return chaine == chaine[::-1]

def ker(chaine):
    return chaine.find("ker") != -1

v = 0
c = 0
for lettre in nom:
    if lettre in voyelles:
        v += 1
    else:
        c += 1

inter = 2*v-c+int(ker(nom))*5
if(inter >= 0 and palindrom(nom)):
    inter *= 2
print(inter)
