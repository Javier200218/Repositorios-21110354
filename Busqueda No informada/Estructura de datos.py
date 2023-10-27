# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:41:27 2023

@author: Javier
"""

# Crear una lista de números
lista_numeros = [5, 10, 15, 20, 25]

# Agregar un elemento al final de la lista
lista_numeros.append(30)

# Acceder a elementos de la lista por índice
primer_elemento = lista_numeros[0]
ultimo_elemento = lista_numeros[-1]

# Modificar un elemento de la lista
lista_numeros[2] = 12

# Obtener la longitud de la lista
longitud = len(lista_numeros)

# Iterar a través de la lista
for numero in lista_numeros:
    print(numero)

# Eliminar un elemento de la lista por valor
if 20 in lista_numeros:
    lista_numeros.remove(20)

# Eliminar un elemento de la lista por índice
indice = lista_numeros.index(15)
del lista_numeros[indice]

# Ordenar la lista en orden ascendente
lista_numeros.sort()

# Reversar la lista
lista_numeros.reverse()

# Crear una lista vacía
lista_vacia = []

# Verificar si la lista está vacía
if not lista_vacia:
    print("La lista está vacía")

# Copiar una lista
copia_lista = lista_numeros.copy()

# Limpiar todos los elementos de la lista
lista_numeros.clear()