#Exercicio54
from time import sleep

credito = dict()

credito["Nome"] = input("Digite o seu nome: ")

credito["Ano Nascimento"] = int(input("Digite o seu ano de nascimento: "))

credito["Rendimento mensal"] = float(input("Digite o seu rendimento mensal: "))

credito["Despesas mensais"] = float(input("Digite as suas despesas mensais: "))

credito["Montante do credito"] = float(input("Digite o motante de credito que deseja: "))

credito["prazo"] = int(input("Digite os anos que pretende ter o credito: "))

#Idade:

credito["idade"] = 2023 - (credito["Ano Nascimento"])
print(f"Idade: {credito['idade']}")

#Remanescente:

credito["remanescente"] = (credito["Rendimento mensal"]) - (credito["Despesas mensais"])
print(f"O remanescente no mês é: {credito['remanescente']}")

#Pagamentomensal

credito["pagamento mensal"] = (credito["Montante do credito"]) / (credito["prazo"] * 12)
print(f"O valor a pagar por mês é de: {credito["pagamento mensal"]}")

#Aprovação

print("Analisando o seu crédito....")
sleep(1)

if credito["remanescente"] > credito["pagamento mensal"]:
    credito["Aprovação"] = "Aprovado"
else:
    credito["Aprovação"] = "Recusado"

print(f"O seu crédito foi {credito["Aprovação"]}")
