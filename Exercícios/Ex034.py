#Exercicio34
cont = 0
opt = ""
maior = 0
menor = 0
media = 0
soma = 0

while True:
    nota = int(input("Digite a sua nota: "))
    cont += 1
    soma += nota
    media = soma / cont
    if maior == menor == 0:
        maior = nota
        menor = nota
    else:
        if nota > maior:
            maior = nota
        elif nota < menor:
            menor = nota
    opt = input("Quer continuar? [S/N]: ").upper().strip()[0]
    if opt in "Nn":
            break
print(f"O seu numero maior inserido foi {maior} e o menor foi {menor}. \n Enquando que a média dos mesmo foi {media}")
