#exercicio29

classificacao = ("Real Madrid", "Girona", "Atl.Madrid", "Barcelona", "Ath.Bilbao", "Real Sociedade", "Betis",
                 "Getafe", "Valencia", "Las Palmas", "Rayo", "Osasuna", "Vilarreal", "Mallorca",
                 "Alaves", "Sevilla", "Cela Vigo", "Cadiz", "Granada", "Almeria")

#a
"""print("1º - ", classificacao[0])
print("2º - ", classificacao[1])
print("3º - ", classificacao[2])
print("4º - ", classificacao[3])
print("5º - ", classificacao[4])"""

for c in classificacao[0:5]:
    print(f"{classificacao.index(c) + 1} - {c}")

#b
print("\n Ultimos 4 classificados")
"""print("17º - ", classificacao[-4])
print("18º - ", classificacao[-3])
print("19º - ", classificacao[-2])
print("20º - ", classificacao[-1])"""

for c in classificacao[-4:]:
    print(f"{classificacao.index(c) + 1} - {c}")

#c
print("\nOrdem alfabetica")

classificacao_ordem_alfabetica = sorted(classificacao)

for c in classificacao_ordem_alfabetica:
    print(c)

#d
print("\nPosição da equipa Las Palmas")
print(f"A equipa Las Plamas esta no lugar ", classificacao.index("Las Palmas") + 1, "º")

