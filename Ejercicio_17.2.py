#Calcular la diferencia entre dos conjuntos
print("\tSean dos conjuntos")

conjunto_1 = {"cuaderno", "libro","lapicero","borrador",34, -89,"cuaderno"}

conjunto_2 = {"ana", "libro", 34, "jose", "manuel", -678,"victor"}

print("Primer conjunto: ", conjunto_1)
print()
print("Segundo conjunto: ", conjunto_2)

print("\n\tDiferencia de conjuntos")
diferencia_1 = conjunto_1 -conjunto_2
print("Diferencia entre el primer conjunto - segundo conjunto: ", diferencia_1)
print()
diferencia_2 = conjunto_2 -conjunto_1
print("Diferencia entre el segundo conjunto - primer conjunto: ", diferencia_2)
