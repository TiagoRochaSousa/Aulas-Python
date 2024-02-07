'''Exercicio 1
print("Hello world", "\n\n")

#Exercicio 2
utilizador = input("Digite o seu nome de utilizador: ")
print("Bem vindo", utilizador, "\n\n")

#Exercicio 3
numero_a = int(input("introduz o primeiro número:"))
numero_b = int(input("introduz o segundo número:"))

def soma_dos_numero(numero_a, numero_b):
        return numero_a + numero_b

resultado = soma_dos_numero(numero_a, numero_b)

print(resultado)

#Exercicio 4
numero_introduzido = int(input("introduz o teu número:"))
print("O antecessor é:", (numero_introduzido-1))
print("O sucessor é:", (numero_introduzido+1))


#Exercicio 5
#Ler numeros do utilizador
num_a = int(input("Digite um numero: "))
num_b = int(input("Digite um numero: "))

#Estruturar as variaveis e calculos
soma = num_a + num_b
subtracao = num_a - num_b
multiplicacao = num_a * num_b
divisao = num_a / num_b
resto = num_a % num_b

#Apresentar resultados no ecrã
print("Soma:", soma)
print("Subtracao:", subtracao)
print("Multiplicacao:", multiplicacao)
print("Divisao:", divisao)
print("Resto:", resto)

#Exercicio 6
#Ler numeros do utilizador
nota1 = float(input("Introduza a primeira nota: "))
nota2 = float(input("Introduza a segunda nota: "))
nota3 = float(input("Introduza a terceira nota: "))
nota4 = float(input("Introduza a quarta nota: "))
nota5 = float(input("Introduza a quinta nota: "))

#Estruturar variaveis
media = (nota1 + nota2 + nota3 + nota4 + nota5)/5

#Apresentar resultados no ecrã
print("A média é: ", media, "valores")

#Exercicio 7
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

print("A idade é: ", idade, "anos")

#Exercicio 8
km_percorridos = float(input("Digite os km percorridos: "))
dias_alogado = int(input("Digite os dias alugados: "))

#calculos
custo_dia = 60
custo_km = 0.456
valor_km = km_percorridos * custo_km
valor_dia = dias_alogado * custo_dia
valor_total = valor_km + valor_dia

#resultado no ecra
print("O valor total pelo aluguer é de:", valor_total, "euros")

#Exerciocio9
nome_completo = input("Digite o seu nome: ")
print("O seu nome em maiusculas é:", nome_completo.upper())
print("O seu nome em minusculas é:", nome_completo.lower())
print(len(nome_completo)-nome_completo.count(" "))
primeiro_nome = nome_completo.find(" ")
print(primeiro_nome)
nome_proprio = nome_completo.split()
print("o seu primeiro nome é {} e tem {} caracteres".format(nome_proprio[0], len(nome_proprio[0])))

#Exercicio10
num = int(input("Introduza um número de 0 a 9999: "))

#Tratar os dados
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#Imprimir no ecrã
print("unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))

#Exercicio11
frase = input("Digite a sua frase:")
frase_minisculas = frase.lower()
print("A letra A aparece {} vezes".format(frase_minisculas.count("a")))
print("A primeira vez que aparece é na posição {}".format(frase_minisculas.find("a")+1))
print("A ultima vez que aparece é na posição {}".format(frase_minisculas.rfind("a")+1))

#Exercicio12
nomeP = input("Digite o seu nome próprio: ")
nomeF = input("Digite o seu ultimo nome: ")
print("Olá", nomeP + " " + nomeF, "o seu registo está criado")

nomeP_email = nomeP[0].lower()
nomeF_email = nomeF.lower()
nome_final = nomeP_email+"."+nomeF_email+"."+"edu@empresa.pt"
print("O seu email é ", nome_final)

#Exercicio13
palavra = input("Digite uma palavra de 6 letras: ")[::-1]
print(palavra)

#Exercicio14
print("=======Radar de velocidade=======", "\n")
num_velocidade = int(input("Introduza a sua velocidade: "))
valor_multa = (num_velocidade-80) * 7 + 100

if (num_velocidade > 80):
    print("Multa :", valor_multa, "euros")
else:
    print("Sem multa, boa viagem!")

#Exercicio15
num_introduzido = int(input("Digite o seu número: "))
if (num_introduzido % 2 == 0):
    print(f"O seu número {num_introduzido} é par")
else:
    print(f"O seu número {num_introduzido} é impar")

#Exercicio16
nota1 = float(input("DIgite a sua nota de calculo1: "))
nota2 = float(input("DIgite a sua nota de calculo2: "))
nota3 = float(input("DIgite a sua nota de Fisica: "))
nota4 = float(input("DIgite a sua nota de Metodos: "))
nota5 = float(input("DIgite a sua nota de biologia: "))

media_nota = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print("A tua média é de ", media_nota)

if (media_nota >= 9.5):
    print(f"Passou de ano com média {media_nota:.2f}, parabéns!")
elif (media_nota >= 8 and media_nota < 9.5):
    print("Vais ter de ir a recurso")
else:
    print("Reprovaste de ano")

#Exercicio17
#Pedir numero ao utilizador
num_introduzido = int(input("Digite o seu numero: ",))

#Ler opçao de escolha
print("Escolha a base de conversão")
print("[1] - Binário")
print("[2] - Octal")
print("[3] - Hexadecimal")
opcao = int(input("Digite a sua opção: "))

#Mostrar a base de conversao
if opcao == 1:
    print(f"O numero {num_introduzido} em Binário é {bin(num_introduzido)[2:]}")
elif opcao == 2:
    print(f"O numero {num_introduzido} em Octal é {oct(num_introduzido)[2:]}")
elif opcao == 3:
    print(f"O numero {num_introduzido} em Hexadecimal é {hex(num_introduzido)[2:]}")
else:
    print("A sua opção é invalida")

#Exercicio18
num1 = int(input("Digite o seu primeiro numero: "))
num2 = int(input("Digite o seu segundo numero: "))

if num1 > num2:
    print(f"O seu primeiro numero introduzido {num1} é maior que o segundo {num2}")
elif num2 == num1:
    print("Os seus numeros sao iguais")
else:
    print(f"O seu primeiro numero introduzido {num1} é menor que o segundo {num2}")

#Exercicio19
print("======JOGO DA ADIVINHA======")
print("O computador vai pensar num número aleatório entre 0 a 7 \n")
num_introduzido = int(input("Digite o número que acha que o computador pensou: "))

#importar biblioteca de generar numero aleatorio
import random
lista = [0, 1, 2, 3, 4, 5, 6, 7]
num_computador = random.choice(lista)

#Condição
if num_computador == num_introduzido:
    print(f"Parabéns você adivinhou os pensamentos do computador, o número é {num_computador}")
else:
    print(f"A IA é muito forte e escolheu o {num_computador} e tu escolheste o {num_introduzido}")

#Exercicio20

#pedra,papel,tesoura
print("======PEDRA, PAPEL, TESOURA======")
print("[1] - PEDRA")
print("[2] - PAPEL")
print("[3] - TESOURA")

#escolha do pc
import random
lista = [1, 2, 3]
escolha_pc = random.choice(lista)

#utilizador
opcao = int(input("Escolha a sua opcao: "))

#importar o time
print("Analisando o resultado....")
import time
time.sleep(3)

#calculos
if opcao == escolha_pc:
    print("Empate")
elif opcao == 1 and escolha_pc == 2:
    print("Perdeu, PAPEL GANHA A PEDRA")
elif opcao == 1 and escolha_pc == 3:
    print("Ganhou, PEDRA GANHA A TESOURA")
elif opcao == 2 and escolha_pc == 1:
    print("Ganhou, PAPEL GANHA A PEDRA")
elif opcao == 2 and escolha_pc == 3:
    print("Perdeu, TESOURA GANHA A PAPEL")
elif opcao == 3 and escolha_pc == 1:
    print("Perdeu, PEDRA GANHA A TESOURA")
else:
    print("Ganhou, TESOURA GANHA A PAPEL")

#mostrar escolha do pc
if escolha_pc == 1:
    print("O pc escolheu a opção PEDRA")
elif escolha_pc == 2:
    print("O pc escolheu a opção PAPEL")
else:
    print("O pc escolheu a opção TESOURA")
'''