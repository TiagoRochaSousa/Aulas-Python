#exercicio53
import operator
from random import randint
from time import sleep

jogada = {"Ricardo": randint(1, 6), "Tiago": randint(1, 6), "Rodrigo": randint(1, 6),
          "Ana": randint(1, 6)}

for n, v in jogada.items():
    print(f"O jogador {n} tirou o {v} no dado")

print("A verificar resultados....")
sleep(1)

jogada_sorted = dict(sorted(jogada.items(), key=operator.itemgetter(1), reverse=True))

print("A ordem de jogada é a seguinte: \n")
sleep(1)

for n, v in jogada_sorted.items():
    if n[-1] == "a":
        print(f"A {n} pois tirou o {v}")
    else:
        print(f"O {n} pois tirou o {v}")
