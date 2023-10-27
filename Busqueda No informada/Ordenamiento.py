# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:41:40 2023

@author: Javier
"""

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Establece un indicador para controlar si se ha realizado algún intercambio en esta iteración
        swapped = False
        
        # Recorre la lista de izquierda a derecha
        for j in range(0, n-i-1):
            # Compara el elemento actual con el siguiente elemento
            if arr[j] > arr[j+1]:
                # Realiza el intercambio
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        # Si no se realizó ningún intercambio en esta iteración, la lista está ordenada
        if not swapped:
            break

# Ejemplo de uso
if __name__ == "__main__":
    # Lista de números desordenados
    numeros = [64, 34, 25, 12, 22, 11, 90]
    
    # Llama a la función de ordenamiento de burbuja
    bubble_sort(numeros)
    
    # Imprime la lista ordenada
    print("Lista ordenada:")
    for numero in numeros:
        print(numero)