"""Encolamos y desencolados elemento"""
from collections import deque

cola = deque()

# Encolamos elementos
cola.append('1')
cola.append('2')
cola.append('3')

print("Cola después de encolar:", list(cola))

# Desencolamos un elemento
elemento = cola.popleft()

print("Elemento desencolado:", elemento)
print("Cola actual:", list(cola))