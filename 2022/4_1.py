cnt = 0
for s in open("input.txt").read().splitlines():
   nr = s.split(",")
   ran1 = nr[0].split("-")
   ran2 = nr[1].split("-")
   if (int(ran1[0]) >= int(ran2[0]) and int(ran1[1]) <= int(ran2[1])) or (int(ran2[0]) >= int(ran1[0]) and int(ran2[1]) <= int(ran1[1])):
       cnt += 1

print(cnt)