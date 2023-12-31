# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:17:08 2023

@author: Javier
"""

import heapq

# Definición del grafo con ciudades y distancias
grafo = {
    'Nueva York': {'Los Ángeles': 2444, 'Chicago': 789, 'Miami': 1288},
    'Los Ángeles': {'Nueva York': 2444, 'Chicago': 1745, 'San Francisco': 348},
    'Chicago': {'Nueva York': 789, 'Los Ángeles': 1745, 'Houston': 1085},
    'Miami': {'Nueva York': 1288, 'Houston': 1187},
    'San Francisco': {'Los Ángeles': 348},
    'Houston': {'Chicago': 1085, 'Miami': 1187},
}

# Función de búsqueda AO*
def ao_star_search(grafo, inicio, destino):
    heap = [(0, inicio, [inicio])]  # Iniciamos con un costo de 0, ciudad de inicio y camino.
    visitados = set()

    while heap:
        costo, ciudad_actual, camino = heapq.heappop(heap)

        if ciudad_actual == destino:
            print("Ruta encontrada:", costo)
            print("Camino:", " -> ".join(camino))
            break

        if ciudad_actual in visitados:
            continue

        visitados.add(ciudad_actual)

        for vecino, distancia in grafo[ciudad_actual].items():
            if vecino not in visitados:
                nuevo_costo = costo + distancia
                nuevo_camino = camino + [vecino]
                heapq.heappush(heap, (nuevo_costo, vecino, nuevo_camino))

# Ejemplo de uso: buscamos la ruta desde "Nueva York" a "Los Ángeles".
ao_star_search(grafo, 'Nueva York', 'Miami')