#função
def soma(a, b):
    s = a + b
    return f'A soma do numero {a} com o numero {b} é {s}'


def multiplica(a, b):
    m = a * b
    return f'A multiplicação do numero {a} com o numero {b} é {m}'


def divide(a, b):
    div = a / b
    return f'A divisão do numero {a} com o numero {b} é {div}'

def subtrai(a, b):
    sub = a - b
    return f'A subtracao do numero {a} com o numero {b} é {sub}'


def tabuada(a):
    for i in range(0, 10):
        resultado = a * (i + 1)
        print(f'{a} x {i + 1} = {resultado}')


def num_par_impar(a):
    if a % 2 == 0:
        return f'O número {a} é par'
    else:
        return f'O número {a} é impar'


def fatorial(num, mostra=False):
    fat = 1
    for f in range(num, 0, -1):
        if mostra:
            if f == 1:
                print(f"{f} = ", end="")
            else:
                print(f"{f} x ", end="")
        fat += f
    return fat

