#Exercicio26
#imports
from datetime import date
ano_atual = date.today().year

#Variaveis de controlo
maiores_idade = 0
menores_idade = 0

#Rodar for para leitura e analise de idades
for c in range(1, 8):
    ano_nascimento = int(input(f"Digite o ano em que a {c} pessoa nasceu: "))
    if ano_atual - ano_nascimento < 18:
        menores_idade += 1
        print("A pessoa é menor de idade")
    else:
        maiores_idade += 1
        print("A pessoa á maior de idade")

#Exibir no ecra os dados
print(f"Existem {menores_idade} pessoas menores de idade e {maiores_idade} maiores de idade")
