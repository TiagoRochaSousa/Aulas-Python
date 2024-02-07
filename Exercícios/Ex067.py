#Exercicio67

def validacao():
    while True:
        numero = input("Digite o numero para a validação: ")
        if numero.isnumeric():
            print("Isso é um número inteiro")
            break
        else:
            print("Isso não é um número inteiro por favor insira novamente")

validacao()
