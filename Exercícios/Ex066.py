#Exercicio66

def fatorial(num, mostra=False):
    fat = 1
    for f in range(num, 0, -1):
        if mostra:
            if f == 1:
                print(f"{f} = ", end="")
            else:
                print(f"{f} x ", end="")
        fat += f
    return fat

#Programa principal

numero = int(input("Insira um numero para o seu fatorial: "))
opcao = input("Deseja ver o processo? [S/N]: ").strip().lower()
if opcao == "s":
    mostra = True
else:
    mostra = False

resultado = fatorial(numero, mostra)
print(resultado)
