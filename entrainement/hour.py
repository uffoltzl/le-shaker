
time = [int(e) for e in input().split(":")]
M = int(input())
H = int(input())

minutes = (time[0]*H+time[1])//M
hh = (minutes//60)%24
mm = minutes%60

print("{}:{}".format(hh, mm))

#localH, localM = map(int, input().split(":"))
