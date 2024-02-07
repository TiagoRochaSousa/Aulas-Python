#função
def soma(a, b):
    s = a + b
    return s


def multiplica(a, b):
    m = a * b
    return m


def divide(a, b):
    div = a / b
    return div

def subtrai(a, b):
    sub = a - b
    return sub


def tabuada(a):
    for i in range(0, 10):
        resultado = a * (i + 1)
        print(f'{a} x {i + 1} = {resultado}')


def num_par_impar(a):
    if a % 2 == 0:
        return f'O número {a} é par'
    else:
        return f'O número {a} é impar'

