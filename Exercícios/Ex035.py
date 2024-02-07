#Exercicio35


while True:
    num = int(input("Introduza um numero para calcularmos a sua tabuada: "))
    if num <= 0:
        print("O seu numero é invalido")
        break
    for c in range(0, 10):
        tabuada = num * (c + 1)
        print(num, "x", c + 1, "=", tabuada)
