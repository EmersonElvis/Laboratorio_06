#Calcular la diferencia simétrica entre 2 conjuntos
print("\tCreando dos conjuntos")
#Funcion crea conjunto y agrega
def crea_conjunto(n):
    conjunto = set()
    for i in range (n):
        elemento = input(f"Elemento {i}: ")
        conjunto.add(elemento)
    return conjunto
#primer conjunto
conjunto_1 = int(input("\n¿Cuantos elementos quiere agregar al conjunto 1?: "))
primer_conjunto = crea_conjunto(conjunto_1)
#segundo conjunto
conjunto_2 = int(input("\n¿Cuantos elementos quiere agregar al conjunto 2?: "))
segundo_conjunto = crea_conjunto(conjunto_2)
#Imprimiendo conjuntos
print(primer_conjunto)
print(segundo_conjunto)
#Realizando diferencia simetrica
print("\n\t Diferencia de conjuntos")
diferencia_sim = primer_conjunto.symmetric_difference(segundo_conjunto)
print("Diferencia simetrica entre el primer conjunto y segundo es: ", diferencia_sim)
