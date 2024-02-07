#Exercicio37

count25 = 0
menos17 = 0
mulheres = 0
menores = 0

while True:
    sexo = input("Digite o seu sexo, [M/F/OUTRO]: ").upper().strip()
    if sexo != "M" and sexo != "F" and sexo != "OUTRO":
        print("Opcao invalida tente novamente")
    idade = int(input("Digite a sua idade: "))
    opcao = input("Pretende continuar? [S/N]: ").upper().strip()
    if idade > 25:
        count25 += 1
    elif idade < 18:
        menores += 1
    if sexo == "F":
        mulheres += 1
    if idade < 17 and sexo == "M":
        menos17 += 1
    if opcao == "N":
        print("Terminou as inscrições")
        break
print(f"Foram inscritas {count25} pessoa(s) com mais de 25 anos")
print(f"Foram inscritas {menos17} homens com menos de 17 anos")
print(f"Foram inscritos {menores} menores de idade")
print(f"Foram inscrita(s) {mulheres} mulher(es)")
