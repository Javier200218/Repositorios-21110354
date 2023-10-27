# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:19:57 2023

@author: Javier
"""

def heuristica_mochila_01(valores, pesos, capacidad_maxima):
    n = len(valores)
    mochila = [0] * n  # Inicialmente, no hemos seleccionado ningún elemento
    capacidad_actual = 0
    valor_total = 0

    for i in range(n):
        if capacidad_actual + pesos[i] <= capacidad_maxima:
            mochila[i] = 1  # Seleccionar el elemento
            capacidad_actual += pesos[i]
            valor_total += valores[i]

    return mochila, valor_total

# Ejemplo de uso
if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    capacidad_maxima = 50

    mochila, valor_total = heuristica_mochila_01(valores, pesos, capacidad_maxima)
    
    print("Elementos seleccionados (1 = seleccionado, 0 = no seleccionado):", mochila)
    print("Valor total de la mochila:", valor_total)