'''Desenvolva um programa que permita ao utilizador calcular
o seu Índice de Massa Corporal (IMC). O programa deve solicitar
ao utilizador a sua altura e o seu peso. De seguida, utilizando
uma função, deve calcular o IMC e o programa deve exibir uma mensagem
com base no valor do IMC calculado.

IMC abaixo de 18,5: Abaixo do peso
IMC entre 18,5 e 24,9: Peso normal
IMC entre 25,0 e 29,9: Sobrepeso
IMC entre 30,0 e 34,9: Obesidade grau 1
IMC entre 35,0 e 39,9: Obesidade grau 2
IMC acima de 40,0: Obesidade grau 3 (obesidade mórbida)'''

def calcula_imc(altura, peso):
    imc = peso / (altura * altura)
    if imc < 18.5:
        return f"Com IMC de {imc:.2f} você está abaixo do peso."
    elif imc <= 18.5 and imc <= 24.9:
        return f"Com IMC de {imc:.2f} você está com o peso normal."
    elif imc <= 25 and imc <= 29.9:
        return f"Com IMC de {imc:.2f} você está com o sobrepeso."
    elif imc <= 30 and imc <= 34.9:
        return f"Com IMC de {imc:.2f} você está com o Obesidade grau 1."
    elif imc <= 35 and imc <= 39.9:
        return f"Com IMC de {imc:.2f} você está com o Obesidade grau 2."
    else:
        return f"Com IMC de {imc:.2f} você está com o Obesidade grau 3 (obesidade mórbida)."

#print(calcula_imc(1.70, 68))
num = 1.75
print(type(num))
if type(num) == float:
    numero = str(num)
    posicao = numero.find(".")
    numero[posicao].replace(".", " ")
    print(numero)
    print(posicao)
