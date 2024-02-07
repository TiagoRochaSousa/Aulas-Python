#Exercicio25 - executar uma frase para indicar se é um palindromo
frase = input("Introduza uma frase: ").strip().upper()
palavras = frase.split()
juntas = "".join(palavras)
inverso = juntas[::-1]
tam = len(juntas)

for c in range(0, tam):
    if juntas[c] != inverso[c]:
        print("Não é um palindromo")
        break
    if c == tam - 1:
        print("é um palindromo")


print(juntas)
print(inverso)
