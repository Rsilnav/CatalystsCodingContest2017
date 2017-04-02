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


f = open("level3/level3-4.txt", "r")

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

trip = int(f.readline())
for t in range(trip):
    trips.append(f.readline().split())

n1, n2 = f.readline().split()

count = 0
for t in trips:
    #print t[0], t[1], n1, n2
    hyperd = tripd(t[0], t[1], n1, n2)
    driving = dista(lc[t[0]], lc[t[1]])/15.0

    print hyperd, driving
    t[2] = int(t[2])

    if  int(round(hyperd)) < t[2] and int(round(hyperd)) < driving:
        count += 1

print count