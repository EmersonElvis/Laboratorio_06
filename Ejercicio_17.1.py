#Realizar operaciones de unión, intersección y diferencia de 2 conjuntos
print("\tCreando dos conjuntos")

def crea_conjunto(n):
    conjunto = set()
    for i in range (n):
        elemento = int(input(f"Elemento solamentos numeros enteros {i}: "))
        conjunto.add(elemento)
    return conjunto

conjunto_1 = int(input("\nCuantos elementos quiere agregar al conjunto_1: "))
primer_conjunto = crea_conjunto(conjunto_1)
print(primer_conjunto)

conjunto_2 = int(input("\nCuantos elementos quiere agregar al conjunto_2: "))
segundo_conjunto = crea_conjunto(conjunto_2)
print(segundo_conjunto)

print("\tRealizando operaciones\n\t Union de conjuntos")
union=primer_conjunto.union(segundo_conjunto)
print("Union de conjuntos 1 y 2 es: ", union)

print("\n\tInterseccion de conjuntos")
interseccion = primer_conjunto.intersection(segundo_conjunto)
print("Interseccion de los conjuntos 1 y 2 es: ", interseccion)

print("\n\t Diferencia de conjuntos")
diferencia_1 = primer_conjunto - segundo_conjunto
print("Diferencia entre el primer conjunto y segundo es: ", diferencia_1)

diferencia_2 = segundo_conjunto - primer_conjunto
print("Diferencia entre el segundo conjunto y primer es: ", diferencia_2)
