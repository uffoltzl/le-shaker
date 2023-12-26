
Q = int(input())
N = int(input())
P = [int(i) for i in input().split()]

def partition(ens):
    possible = []
    autre = []
    for i in range(2**len(ens)):
        res = 0
        aut = []
        somme = 0
        for j in range(len(ens)):
            if (i>>j)&1 == 1:
                res += ens[j]
            else:
                aut.append(ens[j])
                somme += ens[j]
        aut.append(somme)
        autre.append(aut)
        possible.append(res)
    return possible, autre

possible, autre = partition(P)

result = "IMPOSSIBLE"
for i in range(len(possible)):
    if Q == possible[i]:
        if autre[i][-1] < Q:
            result = "POSSIBLE"
            break
        else:
            possibleBob, autreBob = partition(autre[i])
            if not Q in possibleBob:
                result = "POSSIBLE"
                break

print(result)

## amélioration : faire la deuxième partie directement dans la première
