from  random import randint

matriz = []
for i in range(10):
    lista_temporaria = []

    for j in range(10):
        lista_temporaria.append(randint( 1, 1000))
    matriz.append(lista_temporaria)

print(matriz)