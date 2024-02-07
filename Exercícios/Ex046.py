#Exercicio46

lista_um = list()
lista_par = list()
lista_impar = list()

while True:
    num = int(input("Digite um numero: "))
    lista_um.append(num)
    continua = input("Deseja continuar? [S/N]: ").upper().strip()
    if continua == "N":
        break
    if num % 2 == 0:
        lista_par.append(num)
    else:
        lista_impar.append(num)

print(lista_um)
print("Par", lista_par)
print("impar", lista_impar)
