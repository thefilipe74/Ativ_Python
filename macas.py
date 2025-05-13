# Solicita a quantidade de maçãs compradas
quantidade = int(input("Digite o número de maçãs compradas: "))

# Define o preço com base na quantidade
if quantidade < 12:
    preco = 1.30
else:
    preco = 1.00

# Calcula o custo total
custo_total = quantidade * preco

# Exibe o resultado
print(f"O custo total da compra é R$ {custo_total:.2f}")