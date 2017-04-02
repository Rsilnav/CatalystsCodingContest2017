import math
import random


def back(lista, suma_acumulada):
    for city in lc:


f = open("level6/level6-1.txt", "r")

cities = int(f.readline())

lc = {}

trips = []

for city in range(cities):
    temp = f.readline().split()
    #print temp
    x = int(temp[1])
    y = int(temp[2])
    name = temp[0]
    lc[name] = [x, y]


trip = int(f.readline())
for t in range(trip):
    trips.append(f.readline().split())


objetivo = int(f.readline())
metros_maximos = int(f.readline())

lista_actual = lc.keys()[0]

print lista_actual