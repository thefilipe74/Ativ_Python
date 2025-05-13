import time


filmes = [
    ['Interstelar ',2015],
    ['Titanic', 1997],
    ['Star wars: Epsodio ',1983]
]
#Liatar Filmes
def listar_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} - {bd[i][1]} - {bd[i][0]}')


#Cadastrar Filmes
def cadastro_filme (bd, titulo, ano ):
    filme = [titulo, ano]
    filmes.append(filme)
    return bd

#Alterar Filme
#def alterar_filme (bd, titulo, ano ):
 #   indice = filmes.index(titulo,ano)
  #  filmes[indice] = titulo, ano
   # return







while True :
    print(' Bem vindo ao FilFilmes !')
    print ('1 - Cadastrar filme ')
    print ('2 - Alterar Filmes ')
    print ('3 - Listar Filmes')
    print ('0 - sair')
    try:
        op = int(input('Digite a Opção Desejada '))
    except Exception as e:
        print(f'Erro: {e}')
        op = -1

    time.sleep(1)
    #
    if op == 1:
        print('=========CADASTRO DE FILMES==========')
        titulo = input('Digite o nome do novo filme: ')
        ano = int(input('Digite o ano do novo filme: '))
        filmes = cadastro_filme(
            bd = filmes,
        titulo = titulo,
        ano = ano)
        print('======================================\n')

    elif op == 2:
        print('=========ALTERAR FILMES==========')
            listar_filmes(db=filmes)
        i = int(input('Qual fime deseja alterar :'))
        n_titulo = input('Digite o nome titulo :')
        n_ano = int(input('Digite o novo ano :'))

        print('==================================\n')

        
    elif op == 3:
        print('=========LISTA DE FILMES==========')
        listar_filmes(bd = filmes)
        print('==================================\n')

    elif op == 0 :
        print('Saido do Programa...')
        break
    else:
        print('Opçãp Invalida')
