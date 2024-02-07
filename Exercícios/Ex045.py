#exercicio45

lista = list()

for count in range(0, 5):
    num = int(input("Digite um numero: "))
    if count == 0:
        lista.append(num)
        print("Numero adicionado no inicio")
    elif num > lista[-1]:
        lista.append(num)
        print("Adicionado na ultima posição")
    else:
        contador = 0
        while contador < len(lista):
            if num <= lista[contador]:
                lista.insert(contador, num)
                print(f"O numero foi inserido na posição {contador + 1}")
                break
            contador += 1
print(lista)
