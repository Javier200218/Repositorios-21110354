# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 17:45:07 2023

@author: Javier
"""

# Crear un arreglo dinámico (lista en Python)
dynamic_array = []

# Agregar elementos al arreglo
dynamic_array.append(1)
dynamic_array.append(2)
dynamic_array.append(3)

# Acceder a elementos
element = dynamic_array[1]  # Accede al segundo elemento (índice 1)

# Modificar elementos
dynamic_array[0] = 10

# Obtener la longitud del arreglo
length = len(dynamic_array)

# Eliminar elementos
del dynamic_array[1]  # Elimina el segundo elemento

# Imprimir el arreglo
print(dynamic_array)