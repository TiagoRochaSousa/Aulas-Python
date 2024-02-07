"""
Tuples --> ()
Listas --> []
Dicionarios --> {}
"""

"""
Dicionarios:

series = {"titulo":"Game of Thrones", "temp":8}

acrescentar seris["rate"] = 9.6
apagar del series["temp"]

aceder info - value, keys, items

for k, v in series.items():
    print(f"A chave {k} tem {v}")    
"""
"""aluno = {"Nome": "Cesar", "Média": 14}
print(f"O aluno {aluno['Nome']} tem a média de {aluno['Média']} valores")

if aluno["Média"] >= 9.5:
    aluno["Situação"] = "Aprovado"
else:
    aluno["Situação"] = "Reprovado"

print(aluno["Situação"])
print(aluno.items())"""

"""aluno = dict()

aluno["Nome"] = input("Digite o nome do aluno: ")
aluno["Ex001"] = int(input("Digite a nota do ex001: "))
aluno["Ex002"] = int(input("Digite a nota do ex002: "))
aluno["Ex003"] = int(input("Digite a nota do ex003: "))


aluno["Média"] = (aluno["Ex001"] + aluno["Ex002"] + aluno["Ex003"]) / 3

print(aluno.items())

del aluno["Média"]

print(aluno.items())"""

"""cidade = {"Nome": "Porto", "Código": "OPO", "Baixa": "Ribeira", "Rio": "Douro"}

for elemento in cidade.values():
    print(elemento)

for elemento in cidade.keys():
    print(elemento)

for elemento in cidade.items():
    print(elemento)

for k, v in cidade.items():
    print(f"O {k} é {v}")"""

cidade = {"Nome": "Porto", "Código": "OPO", "Baixa": "Ribeira", "Rio": "Douro"}
cidade_2 = {"Nome": "Lisboa", "Código": "LX", "Baixa": "Chiado", "Rio": "Tejo"}

pais = list()
pais.append(cidade)
pais.append(cidade_2)

for c in range(0, len(pais)):
    print(f"Cidade: {pais[c]['Nome']} --> Registada")
