import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def dista(p1, p2):
    return dist(p1[0], p1[1], p2[0], p2[1])

def tripd(start1, start2, n1, n2):
    start1_d = min(dista(lc[start1], lc[n1]), dista(lc[start1], lc[n2]))
    start2_d = min(dista(lc[start2], lc[n1]), dista(lc[start2], lc[n2]))

    d = dista(lc[n1], lc[n2])

    return (start1_d/15.0 + start2_d/15.0 + (d/250.0 + 200.0))

f = open("level5/level5-4.txt", "r")

cities = int(f.readline())

lc = {}

trips = []

for city in range(cities):
    temp = f.readline().split()
    print temp
    x = int(temp[1])
    y = int(temp[2])
    name = temp[0]
    lc[name] = [x, y]

start1, start2 = f.readline().split()

temp = f.readline().split()
hyperlocsnum = int(temp[0])
hyperlocs = temp[1:]

minimo_start = 1000000000000
minimo_start_loc = -1

for i in range(hyperlocsnum):
    dist_temp = dista(lc[start1], lc[hyperlocs[i]])/15.0
    if dist_temp < minimo_start:
        minimo_start = dist_temp
        minimo_start_loc = i

print hyperlocs[minimo_start_loc],minimo_start 

minimo_end = 1000000000000
minimo_end_loc = -1

for i in range(hyperlocsnum):
    dist_temp = dista(lc[start2], lc[hyperlocs[i]])/15.0
    if dist_temp < minimo_end:
        minimo_end = dist_temp
        minimo_end_loc = i

if minimo_start_loc > minimo_end_loc:
    minimo_end_loc, minimo_start_loc = minimo_start_loc, minimo_end_loc

puntero = minimo_start_loc
suma = 0.0
print puntero, minimo_end_loc
while (puntero < minimo_end_loc):
    #print hyperlocs[puntero], hyperlocs[puntero+1]
    suma += dista(lc[hyperlocs[puntero]], lc[hyperlocs[puntero+1]])/250.0 + 200.0
    #print dista(lc[hyperlocs[puntero]], lc[hyperlocs[puntero+1]])

    puntero += 1

print int(round(suma+minimo_start+minimo_end))



'''

trip = int(f.readline())
for t in range(trip):
    trips.append(f.readline().split())


objetivo = int(f.readline())

flag = True
for start_key in lc:
    if not flag:
        break
    for end_key in lc:


        count = 0
        for t in trips:
            #print t[0], t[1], n1, n2
            hyperd = tripd(t[0], t[1], start_key, end_key)
            driving = dista(lc[t[0]], lc[t[1]])/15.0

            #print hyperd, driving
            t[2] = int(t[2])

            if int(round(hyperd)) < t[2] and int(round(hyperd)) < driving:
                count += 1

        if count >= objetivo:
            print start_key, end_key

            flag = False
            break

print "Termine"

'''