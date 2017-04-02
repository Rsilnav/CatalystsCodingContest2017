import math

f = open("level1/level1-1.txt", "r")

cities = int(f.readline())

list_cities = {}

for city in range(cities):
    temp = f.readline().split()
    print temp
    x = int(temp[1])
    y = int(temp[2])
    name = temp[0]
    list_cities[name] = [x, y]

n1, n2 = f.readline().split()

d = math.sqrt((list_cities[n1][0] - list_cities[n2][0])**2 + (list_cities[n1][1] - list_cities[n2][1])**2)
print int(round(d/250 + 200))