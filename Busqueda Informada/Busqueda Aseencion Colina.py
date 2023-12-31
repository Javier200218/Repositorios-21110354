# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:17:59 2023

@author: Javier
"""

# Definición del grafo con ciudades y distancias
grafo = {
    'Nueva York': {'Los Ángeles': 2444, 'Chicago': 789, 'Miami': 1288},
    'Los Ángeles': {'Nueva York': 2444, 'Chicago': 1745, 'San Francisco': 348},
    'Chicago': {'Nueva York': 789, 'Los Ángeles': 1745, 'Houston': 1085},
    'Miami': {'Nueva York': 1288, 'Houston': 1187},
    'San Francisco': {'Los Ángeles': 348},
    'Houston': {'Chicago': 1085, 'Miami': 1187},
}

# Función de búsqueda de ascenso a la colina
def hill_climbing(grafo, inicio, destino):
    ciudad_actual = inicio  # Comenzamos en la ciudad de inicio.
    camino = [ciudad_actual]  # Inicializamos el camino con la ciudad de inicio.
    distancia_total = 0

    while ciudad_actual != destino:  # Continuamos hasta que lleguemos al destino.
        vecinos = grafo[ciudad_actual]  # Obtenemos los vecinos de la ciudad actual.
        mejor_vecino = None
        menor_distancia = float('inf')  # Inicializamos la distancia mínima como infinito.

        # Buscamos el vecino más cercano que no haya sido visitado.
        for vecino, distancia in vecinos.items():
            if vecino not in camino and distancia < menor_distancia:
                mejor_vecino = vecino
                menor_distancia = distancia

        if mejor_vecino is None:
            print("No se pudo encontrar una ruta al destino.")
            break

        # Movemos a la ciudad más cercana y actualizamos el camino y la distancia total.
        ciudad_actual = mejor_vecino
        camino.append(ciudad_actual)
        distancia_total += menor_distancia

    if ciudad_actual == destino:
        print("Ruta encontrada:", distancia_total)
        print("Camino:", " -> ".join(camino))

# Ejemplo de uso: buscamos la ruta desde "Nueva York" a "Los Ángeles".
hill_climbing(grafo, 'Nueva York', 'Houston')