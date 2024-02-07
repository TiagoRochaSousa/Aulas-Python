#Exercicio47

lista = list()

while True:
    equa = input("Digite a sua equação: ")
    lista.append(equa)
    resposta = input("S/N")
    if resposta == "N":
        break
print(equa.count("("))

print(lista)