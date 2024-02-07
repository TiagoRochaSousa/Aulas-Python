"""help(print)

primeira = "Olá"
segunda = "Mundo"

print(primeira, segunda, sep="_", end=" TERMINOU")"""

"""import random

help(random)"""

'''def soma(a, b):
    """
    -> This function prints de sum between 2 variables
    :param a: first number
    :param b: second number
    :return: no return
    """
    s = a + b
    print(f"A soma entre {a} e {b} é igual a {s}")

soma(10, 15)
print("*" * 10)
print("UTILIZAR HELP")
help(soma)
'''

'''def escopo(b):
    global a
    a = 8
    b += 5
    c = 3
    print(f"A dentro vale {a}")
    print(f"B dentro vale {b}")
    print(f"C dentro vale {c}")

a = 6
escopo(a)
print(f"A fora vale {a}")'''

def soma(a=0, b=0, c=0):
    """
    -> Sum
    :param a: first number
    :param b: second number
    :param c: third number
    :return:
    """
    s = a + b + c
    return s


resultado = soma(1, 2, 3)
resultado2 = soma(75, 45, 52)
print(f"A primeira soma vale {resultado} e a segunda vale {resultado2}")
