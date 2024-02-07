#Exercicio24 programa que leio se o numero é primo
num = int(input("Introduza um numero inteiro: "))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1                  #igual a tot=tot +1

if tot == 2:
    print(f"O número {num} é primo, foi divisivel {tot} vezes")
else:
    print(f"O número {num} não é primo, foi divisil {tot} vezes")
