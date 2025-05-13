salario = float(input("Informe seu salario:"))


if 0 < salario <= 2000:
    print(f'Salario sem imposto! R$:{salario}')
elif 2000.00 < salario <= 3500.00:
    imposto = salario * 0.10
    print(f'Seu imposto sera de R${imposto}')
    print(f'Seu salario é no valor de R$ {salario}')
elif salario > 3500.00:
    imposto = salario * 0.15
    print(f'Seu imposto sera de R${imposto}')
    print(f'Seu salario é no valor de R$ {salario}')
