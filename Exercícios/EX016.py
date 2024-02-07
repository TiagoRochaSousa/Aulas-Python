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
