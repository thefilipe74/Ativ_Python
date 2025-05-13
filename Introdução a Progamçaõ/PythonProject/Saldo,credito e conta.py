'''============================='''

conta = int(input("Insira o numero da sua conta : "))
saldo = int(input("Insira seu saldo atual  : "))
debito = int(input("Informe o quanto voce gastou : "))
credito = int(input("informe o quanto voce recebel :"))

saldoAtual = (saldo - debito + credito)

'''=============================='''

print("Essa são as informações da sua conta :")
print("CONTA : ", conta)
print("SALDO ATUAL : ", saldoAtual)
print("DEBITO : ", debito)
print("CREDITO : ", credito)

'''==============================='''
if: saldoAtual <= 0    print("seu saldo atual é negativo",saldoAtual)
else:
    print("seu saldo é positivo", saldoAtual)
