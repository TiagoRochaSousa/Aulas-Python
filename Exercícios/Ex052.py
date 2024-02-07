#Exercicio52

aluno = {}

aluno["Nome"] = input("Digite o seu nome: ")
aluno["Média"] = float(input(f"Média de {aluno['Nome']}: "))

if aluno["Média"] >= 9.5:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

print(f"O aluno {aluno['Nome']} tem uma média de {aluno['Média']} e encontra-se {aluno['Situação']}")
