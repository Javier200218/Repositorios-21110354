# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 18:09:45 2023

@author: Javier
"""

# Función de ordenamiento usando el método sort de lista
def sort_list(input_list):
    sorted_list = sorted(input_list)
    return sorted_list

# Función de búsqueda binaria en una lista ordenada
def binary_search(sorted_list, target):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid  # Elemento encontrado, devuelve el índice
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Elemento no encontrado, devuelve -1

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    numeros = [64, 34, 25, 12, 22, 11, 90]

    # Llama a la función de ordenamiento
    numeros_ordenados = sort_list(numeros)
    print("Lista ordenada:", numeros_ordenados)

    # Llama a la función de búsqueda binaria
    elemento_buscar = 22
    resultado_busqueda = binary_search(numeros_ordenados, elemento_buscar)
    
    if resultado_busqueda != -1:
        print(f"{elemento_buscar} encontrado en el índice {resultado_busqueda}.")
    else:
        print(f"{elemento_buscar} no encontrado en la lista.")