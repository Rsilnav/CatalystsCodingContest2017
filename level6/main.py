import math
import random

def distancia_lista_ciudades(lista):
    suma = 0
    for l in range(len(lista)-1):
        c1 = lc[lista[l]]
        c2 = lc[lista[l+1]]
        suma += dista(c1, c2)
    return suma

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def dista(p1, p2):
    return dist(p1[0], p1[1], p2[0], p2[1])

def tripd(start1, start2, n1, n2):
    start1_d = min(dista(lc[start1], lc[n1]), dista(lc[start1], lc[n2]))
    start2_d = min(dista(lc[start2], lc[n1]), dista(lc[start2], lc[n2]))

    d = dista(lc[n1], lc[n2])

    return (start1_d/15.0 + start2_d/15.0 + (d/250.0 + 200.0))

f = open("level6/level6-3.txt", "r")

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


solved = False
vueltas = 0
while not solved and vueltas < 1000000:
    vueltas += 1
    #solved = True

    num_cities = random.randint(2, len(lc.keys()))
    lista = random.sample(lc.keys(), num_cities)
    #num_cities = 2
    #lista = ["Budapest", "Bratislava"]
    distancia_acumulada = distancia_lista_ciudades(lista) 
    if distancia_acumulada > metros_maximos:
        continue

    #print "Tiempo en la red", dista(lc[lista[0]], lc[lista[0+1]])/250.0 + 200.0


    #print lista

    count = 0
    for t in trips:

        minimo_start = 1000000000000
        minimo_start_loc = -1

        for i in range(num_cities):
            dist_temp = dista(lc[t[0]], lc[lista[i]])/15.0
            if dist_temp < minimo_start:
                minimo_start = dist_temp
                minimo_start_loc = i

        #print lista[minimo_start_loc],minimo_start 

        minimo_end = 1000000000000
        minimo_end_loc = -1

        for i in range(num_cities):
            dist_temp = dista(lc[t[1]], lc[lista[i]])/15.0
            if dist_temp < minimo_end:
                minimo_end = dist_temp
                minimo_end_loc = i

        if minimo_start_loc == minimo_end_loc:
            continue

        if minimo_start_loc > minimo_end_loc:
            minimo_end_loc, minimo_start_loc = minimo_start_loc, minimo_end_loc

        puntero = minimo_start_loc
        suma = 0.0
        #print puntero, minimo_end_loc
        while (puntero < minimo_end_loc):
            #print lista[puntero], lista[puntero+1]
            suma += dista(lc[lista[puntero]], lc[lista[puntero+1]])/250.0 + 200.0
            #print dista(lc[lista[puntero]], lc[lista[puntero+1]])
            puntero += 1

        tiempo_en_hyperloop = int(round(suma+minimo_start+minimo_end))
        driving = int(round(dista(lc[t[0]], lc[t[1]])/15.0))

        #print "En hyper", tiempo_en_hyperloop
        #print "Driving", driving

        
        if tiempo_en_hyperloop < int(t[2]) and tiempo_en_hyperloop < driving:
            #print "#", tiempo_en_hyperloop, driving, t[2]
            count += 1


    if count >= objetivo:
        print len(lista), ' '.join(lista), count
        solved = True


print "Termine"
