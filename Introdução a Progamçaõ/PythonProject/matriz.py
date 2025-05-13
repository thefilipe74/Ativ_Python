matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
                     ]

#imprimindo matriz
print(matriz)

#Imprimindo matriz 1

print(matriz[1][2])

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f'i= {i} e j={j} - {matriz[i][j]}')


