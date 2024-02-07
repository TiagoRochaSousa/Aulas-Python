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
