#POR:   Kevin Jaramillo, Jean Carlo Martinez, Cristhian Giron, Keyner Manchay
        #Ceilia Trueba, Gustavo Pineda
#CURSO: Paralelo A
#MATERIA: Complejidad Computacional
#FECHA: 09/02/2022
import os

Nodo = dict() #Creamos un diccionario.
            #Un diccionario es una colección desordenada, modificable e indexada.
resultado = {}
conjuntos = []

def Hacer_conjunto(vertice):
    Nodo[vertice] = vertice

def Encontrar_conjunto(vertice):
    if Nodo[vertice] != vertice:
        Nodo[vertice] = Encontrar_conjunto(Nodo[vertice])
    return Nodo[vertice]

def Union(u, v, Ordenada):
    print("Conjuntos separados:", u, v)
    if u not in conjuntos:
        print(u, "No existe en conjuntos")
        conjuntos.append(u)
    else:
        print(u, "Si existe en conjuntos")
    if v not in conjuntos:
        print(v, "No existe en conjuntos")
        conjuntos.append(v)
    else:
        print(v, "Si existe en conjuntos")
    print("Conjuntos unidos:", conjuntos)

    Dato1 = Encontrar_conjunto(u)
    Dato2 = Encontrar_conjunto(v)
    if Dato1 != Dato2:
        for Dato in Ordenada:
            Nodo[Dato1] = Dato2

def Kruskal(grafo):
    resultante = []
    cont = 0
    for vertice in grafo['A']:
        Hacer_conjunto(vertice)

    Ordenada = list(grafo['B'])
    Ordenada.sort()
    Ordenada = [(a,b,c) for c,a,b in Ordenada]
    print("==============================")
    print("DATOS ORDENADOS:")
    print("==============================")
    print("ORDENADOS:", Ordenada)
    Ordenada = [(c,a,b) for a,b,c in Ordenada]
    for Dato in Ordenada:
        peso, u, v = Dato
        if Encontrar_conjunto(u) != Encontrar_conjunto(v):
            resultante.append(Dato)
            print("==============================")
            print("PASO Nro.", cont)
            print("==============================")
            resultante = [(a,b,c) for c,a,b in resultante]
            print("RESULTANTE : ", resultante)
            resultante = [(c,a,b) for a,b,c in resultante]
            cont+=1

            Union(u, v, Ordenada)

    return resultante

#Definimos nuestro ejercicio a trabajar:
grafo = {
        'A': ['A','B','C','D','E'],
        'B': [  (4, 'A', 'B'),
                (8, 'B', 'C'),
                (10, 'C', 'D'),
                (12, 'D', 'E'),
                (5, 'A', 'E'),
                (9, 'A', 'C'),
                (11, 'A', 'D'),
                (6, 'B', 'E'),
            ]
        }

#Algoritmo de Kruskal
resultante = Kruskal(grafo)
resultante = [(a,b,c) for c,a,b in resultante]
for origen,destino,peso in resultante:
    if origen in resultado:
        if destino in resultado:
            lista = resultado[origen]
            resultado[origen] = lista+[(destino,peso)]
            lista = resultado[destino]
            lista.append((origen,peso))
            resultado[destino] = lista
        else:
            resultado[destino] = [(origen,peso)]
            lista = resultado[origen]
            lista.append((destino,peso))
            resultado[origen] = lista
    elif destino in resultado:
        resultado[origen] = [(destino,peso)]
        lista = resultado[destino]
        lista.append((origen,peso))
        resultado[destino] = lista
    else:
         resultado[destino] = [(origen,peso)]
         resultado[origen] = [(destino,peso)]

print("\n=========RESULTADOS=========")
print("ARBOL DE EXPANSION MINIMA:")
for key, lista in resultado.items():
    print(key)
    print(lista)
print("==============================")
os.system("pause")