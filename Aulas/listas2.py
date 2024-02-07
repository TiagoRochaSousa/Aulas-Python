"""aluno = list()
aluno.append("Tiago")
aluno.append(30)

turma = list()
turma.append(aluno)

aluno[0] = "Amanda"
aluno[1] = 30

print(aluno)
print(turma)"""

"""turma = list()
aluno = list()

for c in range(0, 3):
    aluno.append(input("Digite o nome do aluno: "))
    aluno.append(int(input("Digite a idade: ")))
    turma.append(aluno[:])
    aluno.clear()"""


"""for aluno in turma:
    print(f"O aluno {aluno[0]} tem {aluno[1]} anos")"""

"""for i, a in enumerate(turma):
    print(f"O {i + 1} aluno é o {a}")"""

"""for i in range(0, len(turma)):
    for aluno in range(0, len(turma[0])):
        print(f"{i+1}O aluno {turma[i][aluno]}")"""
