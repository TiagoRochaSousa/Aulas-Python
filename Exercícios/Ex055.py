#Exercicio55
from time import sleep


aproveitamento = dict()

aproveitamento["Nome"] = input("Digite o nome do jogador: ")

aproveitamento["Jogos"] = int(input(f"Quantos jogos jogou o {aproveitamento['Nome']}: "))

aproveitamento["Golos"] = int(input(f"Nos {aproveitamento['Jogos']} jogos o {aproveitamento['Nome']} marcou:  "))

aproveitamento["média de golos"] = (aproveitamento['Golos']) / (aproveitamento['Jogos'])

sleep(1)
print(f"O {aproveitamento['Nome']} tem um média de {aproveitamento['média de golos']} por jogo.")
