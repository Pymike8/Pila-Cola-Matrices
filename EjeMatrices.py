"""Ejemplo de suma y multiplicación de matreices"""
import numpy as np

# Definimos dos matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Sumar matrices
suma = A + B

# Multiplicar matrices
multiplicacion = np.dot(A, B)

print("Matriz A:\n", A)
print("Matriz B:\n", B)
print("Suma:\n", suma)
print("Multiplicación:\n", multiplicacion)