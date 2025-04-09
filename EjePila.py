"""Apilamos y desapilamos elementos"""
pila = []

# Apilamos elementos
pila.append('A')
pila.append('B')
pila.append('C')

print("Pila después de apilar:", pila)

# Desapilamos un elemento
elemento = pila.pop()

print("Elemento desapilado:", elemento)
print("Pila actual:", pila)