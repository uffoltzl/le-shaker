
X_R, X_M = map(int, input().split())
N = int(input())

bus = []
en_voiture = 0

# on s'occupe uniquement des voitures car elles sont prioritaires
for _ in range(N):
    entry = input().split()
    if(entry[0] == 'v'):
        if(entry[1] == 'm'):
            if(int(entry[2]) > X_M and X_M != 0):
                en_voiture += X_M
                X_M = 0
            elif(int(entry[2]) <= X_M):
                en_voiture += int(entry[2])
                X_M -= int(entry[2])
        elif(entry[1] == 'r'):
            if(int(entry[2]) > X_R and X_R != 0):
                en_voiture += X_R
                X_R = 0
            elif(int(entry[2]) <= X_R):
                en_voiture += int(entry[2])
                X_R -= int(entry[2])
    elif(entry[0] == 'b'):
        bus.append(int(entry[1]))


#def fc(i):
#    b = 0
#    rouge = X_R
#    marron = X_M
#    j = 0
#    while(i):
#        res = i%2
#        i = i//2
#        if(res):
#            if(bus[j] > rouge and rouge != 0):
#                b += rouge
#                rouge = 0
#            elif(bus[j] <= rouge):
#                b += bus[j]
#                rouge -= bus[j]
#        else:
#            if(bus[j] > marron and marron != 0):
#                b += marron
#                marron = 0
#            elif(bus[j] <= marron):
#                b += bus[j]
#                marron -= bus[j]
#        j += 1
#
#    return b, (rouge+marron)

#en_bus = 0
#rien = 0
#for i in range(2**len(bus)):
#    b, r = fc(i)
#    if(r == 0):
#        en_bus = b
#        rien = 0
#        break
#    elif(i == 0 or rien > r):
#        en_bus = b
#        rien = r


# on s'occupe des bus
def fc_rec(rouge, marron, b, i):
    if(i >= len(bus) or rouge+marron == 0):
        return (rouge+marron), b

    r_r, r_b = rouge, b
    m_m, m_b = marron, b

    if(rouge == 0):
        if(bus[i] > marron):
            m_b += marron
            m_m = 0
        elif(bus[i] <= marron):
            m_b += bus[i]
            m_m -= bus[i]
        return fc_rec(0, m_m, m_b, i+1)
    elif(marron == 0):
        if(bus[i] > rouge):
            r_b += rouge
            r_r = 0
        elif(bus[i] <= rouge):
            r_b += bus[i]
            r_r -= bus[i]
        return fc_rec(r_r, 0, r_b, i+1)

    if(bus[i] > rouge):
        r_b += rouge
        r_r = 0
    elif(bus[i] <= rouge):
        r_b += bus[i]
        r_r -= bus[i]
    if(bus[i] > marron):
        m_b += marron
        m_m = 0
    elif(bus[i] <= marron):
        m_b += bus[i]
        m_m -= bus[i]
    r_rien, r_b = fc_rec(r_r, marron, r_b, i+1)
    if(r_rien == 0):
        return 0, r_b
    m_rien, m_b = fc_rec(rouge, m_m, m_b, i+1)
    if(r_rien > m_rien):
        return m_rien, m_b
    else:
        return r_rien, r_b

rien, en_bus = fc_rec(X_R, X_M, 0, 0)

print(rien, en_voiture, en_bus)
