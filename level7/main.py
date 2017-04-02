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

f = open("level7/level7-eg.txt", "r")

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

hub = f.readline().strip()

num_lanes = int(f.readline())
lanes = []
for i in range(num_lanes):
    temp = f.readline().split()
    lanes.append(temp[1:])

minimo_start = 1000000000000
minimo_start_loc = -1
minimo_start_lane = -1

for i in range(len(lanes)):
    for j in range(len(lanes[i])):
        dist_temp = dista(lc[start1], lc[lanes[i][j]])/15.0
        if dist_temp < minimo_start:
            minimo_start = dist_temp
            minimo_start_loc = j
            minimo_start_lane = i

minimo_end = 1000000000000
minimo_end_loc = -1
minimo_end_lane = -1

for i in range(len(lanes)):
    for j in range(len(lanes[i])):
        dist_temp = dista(lc[start2], lc[lanes[i][j]])/15.0
        if dist_temp < minimo_end:
            minimo_end = dist_temp
            minimo_end_loc = j
            minimo_end_lane = i

if minimo_start_loc > minimo_end_loc:
    minimo_end_loc, minimo_start_loc = minimo_start_loc, minimo_end_loc
    minimo_end_lane, minimo_start_lane = minimo_start_lane, minimo_end_lane

'''
tiempo_to_hub = dista(lc[lanes[minimo_start_lane][minimo_start_loc]], lc[hub])
tiempo_to_hub2 = dista(lc[lanes[minimo_end_lane][minimo_end_loc]], lc[hub])

print "#", lanes[minimo_start_lane], hub
print tiempo_to_hub/15.0
print tiempo_to_hub2/15.0
print 
'''

puntero = minimo_start_loc
suma = 0.0
print puntero, minimo_end_loc
while (lanes[minimo_start_lane][puntero] != hub):
    suma += dista(lc[lanes[minimo_start_lane][puntero]], lc[lanes[minimo_start_lane][puntero+1]])/250.0 + 200.0
    puntero += 1
tiempo_to_hub = int(round(suma+minimo_start+minimo_end))
print tiempo_to_hub

puntero = minimo_end_loc
suma = 0.0
print puntero, minimo_end_loc
while (lanes[minimo_start_lane][puntero] != hub):
    suma += dista(lc[lanes[minimo_start_lane][puntero]], lc[lanes[minimo_start_lane][puntero+1]])/250.0 + 200.0
    puntero += 1
tiempo_to_hub = int(round(suma+minimo_start+minimo_end))
print tiempo_to_hub