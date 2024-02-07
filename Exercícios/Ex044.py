#Exercicio44

lista_um = list()

while True:
    num = int(input("Digite um numero: "))
    if num in lista_um:
        print("Digite novo numero")
    else:
        lista_um.append(num)
    continua = input("Deseja continuar? [S/N]: ").upper().strip()
    if continua == "N":
        break

lista_um.sort(reverse=True)

for v in lista_um:
    print(v)









