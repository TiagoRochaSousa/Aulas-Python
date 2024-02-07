"""import time

print("="*25)
print("Índice de massa corporal")
print("="*25)

#inputs utilizador
peso = float(input("Digite o seu peso em kg: "))
altura = float(input("Digite a sua altura em m: "))
if altura > 3:
    altura = altura / 100

imc = peso / (altura * altura)

print("A calcular o seu IMC!!")
time.sleep(2)

#condições
if imc < 18.5:
    print(f"O seu IMC é {round(imc, 2)} e está abaixo do peso")
elif imc < 24.9:
    print(f"O seu IMC é {round(imc, 2)} e está com peso normal")
elif imc < 29.9:
    print(f"O seu IMC é {round(imc, 2)} e está em Sobrepeso")
elif imc < 34.9:
    print(f"O seu IMC é {round(imc, 2)} e está com Obesidade grau 1")
elif imc < 39.9:
    print(f"O seu IMC é {round(imc, 2)} e está com Obesidade grau 2")
else:
    print(f"O seu IMC é {round(imc, 2)} e está com Obesidade grau 3 (obesidade mórbida)")"""
