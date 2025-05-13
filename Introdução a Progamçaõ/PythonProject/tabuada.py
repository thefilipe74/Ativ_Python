
numero = int(input("Digite um número para ver a tabuada: "))

with open("tabuada.txt", "w") as arquivo:
    arquivo.write(f"Tabuada do {numero}\n")
    arquivo.write("-" * 20 + "\n")


    for i in range(1, 11):
        resultado = numero * i
        linha = f"{numero} x {i} = {resultado}\n"
        arquivo.write(linha)

print("Tabuada salva no arquivo 'tabuada.txt'.")

