# Solicita o salário mensal ao usuário
salario = float(input("Digite seu salário mensal: R$ "))

# Calcula o imposto de acordo com a faixa salarial
if salario <= 2000:
    imposto = 0
elif salario <= 3500:
    imposto = salario * 0.10
else:
    imposto = salario * 0.15

# Exibe o resultado
print(f"O imposto de renda a ser pago é R$ {imposto:.2f}")
