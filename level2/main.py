import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def dista(p1, p2):
    return dist(p1[0], p1[1], p2[0], p2[1])


f = open("level2/level2-2.txt", "r")

cities = int(f.readline())

list_cities = {}

for city in range(cities):
    temp = f.readline().split()
    print temp
    x = int(temp[1])
    y = int(temp[2])
    name = temp[0]
    list_cities[name] = [x, y]

start1, start2 = f.readline().split()
n1, n2 = f.readline().split()


start1_d = min(dista(list_cities[start1], list_cities[n1]), dista(list_cities[start1], list_cities[n2]))
start2_d = min(dista(list_cities[start2], list_cities[n1]), dista(list_cities[start2], list_cities[n2]))

d = dista(list_cities[n1], list_cities[n2])

print start1_d/15.0, start2_d/15.0, (d/250.0 + 200.0)

print int(round(start1_d/15.0 + start2_d/15.0 + (d/250.0 + 200.0)))