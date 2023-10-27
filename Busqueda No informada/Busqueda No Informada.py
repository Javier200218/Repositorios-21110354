# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:39:56 2023

@author: Javier
"""

from queue import Queue

# Busqueda de anchura
def busqueda_anchura(grafo, inicio, fin):
    visited = [0] * grafo.num_vertices
    cola = Queue()
    cola.put(inicio)
    found_place = 0
    camino = []

    while not cola.empty():
        place = cola.get()
        adyacente = grafo.lista_adyacencia[place]

        while adyacente:
            if adyacente.dato != fin:
                cola.put(adyacente.dato)
                adyacente = adyacente.next
            else:
                found_place = 1
                break

        if found_place == 1:
            visited.append(place)
            camino = [str(x) for x in visited]
            return '->'.join(camino)

        visited.append(place)

# Busqueda de anchura de costo uniforme
def busqueda_anchura_costo_uniforme(grafo, inicio, fin):
    visited = [0] * grafo.num_vertices
    cola = Queue()
    cola.put(inicio)
    found_place = 0

    while not cola.empty():
        place = cola.get()
        adyacente = grafo.lista_adyacencia[place]

        while adyacente:
            if adyacente.dato != fin:
                cola.put(adyacente.dato)
                adyacente = adyacente.next
            else:
                found_place = 1
                break

        visited.append(place)

    return visited