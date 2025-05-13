
'''notas = []

for i in range(6):
    nota = float(input(f'Digite a nota{i+1}:'))
    notas.append(nota)

#Imprimir Todas As Notas!

print('notas digitadas', notas)

#Imprimir Media

media = sum(notas) / len(notas)
print(f' A media das notas são: {media}')
'''

controle = True
notas = []

while controle:
    print('Digite 100 para SAIR ')
    print('ou digite a nota desejada!')

    nota = int(input('Digite a nota : '))
    if 0 <= nota <=10 :
        notas.append(nota)
    elif nota == 100 :
        controle = False
    else:
        print('Valor invalido')