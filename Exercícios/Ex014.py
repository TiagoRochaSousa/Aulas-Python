print("=======Radar de velocidade=======", "\n")
num_velocidade = int(input("Introduza a sua velocidade: "))
valor_multa = (num_velocidade-80) * 7 + 100

if (num_velocidade > 80):
    print("Multa :", valor_multa, "euros")
else:
    print("Sem multa, boa viagem!")
