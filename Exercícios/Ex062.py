#Exercicio62

from time import sleep

#funcao

def pauta(nome, lista_notas):
    print("*" * 30)
    print(f"PAUTA DO ALUNO")
    print("*" * 30)
    soma_notas = 0
    for notas in lista_notas:
        soma_notas += notas

    media = soma_notas / len(lista_notas)
    situacao = "Aprovado" if media >= 9.5 else "Reprovado"
    sleep(1)
    print(f"Média : {media}")
    sleep(1)
    print(f"Situação : {situacao}")


#Código principal

notas = list()
resposta= 0
estudante = input("Digite o seu nome: ")

while True:
    grades = int(input("Digite a sua nota: "))
    notas.append(grades)
    resposta = input("Deseja colocar outra nota? [S/N]: ").upper().strip()
    if resposta == "N":
        break

pauta(estudante, notas)
