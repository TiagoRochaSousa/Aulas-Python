#Exercicio27

#variaveis de controlo
maior_idade = 0
menor_idade = 0

for pessoa in range(1, 11):
    idade = int(input(f"Digite a idade da pessoa {pessoa}: "))
    if pessoa == 1:
        maior_idade = idade
        menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        elif idade < menor_idade:
            menor_idade = idade

print(f"maior idade {maior_idade}, menor idade {menor_idade}")
