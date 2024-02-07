# Exercicio58

def boas_vindas(msg):
    print("***************")
    print(msg)
    print("***************")


def area(c, l):
    a = c * l
    print(f"A área do terreno que colocou é de {a} metros quadrados")


# Codigo principal
boas_vindas("Área do Terreno")
compr = int(input("Digite o comprimento do seu terreno: "))
larg = int(input("Digite a largura do seu terreno: "))
area(compr, larg)
