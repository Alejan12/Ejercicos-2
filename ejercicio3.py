numeros=[1,2,3,4,5,6,7,8,9,2,5,7,4,8,6,4,11,4]
print("Esta es tu lista inicial")
print(numeros)
def modificar(numeros):
    for i in range(len(numeros)-1,-1,-1):
        if numeros[i] in numeros[:i]:
            del numeros[i]
    print("Esta es tu lista sin numeros repetidos")
    print(numeros)
    mayor_menor=sorted(numeros,reverse=True)
    print("Ordenado de mayor a menor")
    print(mayor_menor)
    for i in range(len(numeros)-1,-1,-1):
        if numeros[i]%2!=0:
            del numeros[i]
    print("Solo numeros pares")
    print(numeros)
    suma=sum(numeros)
    print("La suma de todos los numeros que quedan en la liata")
    print(suma)
    numeros.insert(0,suma)
    print("Esta es la lista final añadiendo la suma anterior al principio de la lista")
    print(numeros)

modificar(numeros)