#Exercicio56

dados = dict()
lista = list()

while True:
    dados["Nome"] = input("Digite o seu nome: ")
    dados["Sexo"] = input("Digite o seu sexo: ")
    dados["idade"] = int(input("Digite a sua idade: "))
    continuar = input("Deseja continuar? [S/N]: ").upper().strip()
    if continuar == "N":
        break

