#Exercicio65

from datetime import datetime

def boas_vindas(msg):
    print("*" * 50)
    print(msg)
    print("*" * 50)


def ano_nascimento(ano_nasc):
    idade = datetime.now().year - ano_nasc
    if idade > 18:
        return f"O cidadão tem {idade} e pode tirar a carta"
    elif 18 > idade >= 16:
        return f"O cidadão tem {idade} e tem de pedir autorização"
    else:
        return f"O cidadão tem {idade} e não pode tirar a carta"


ano = int(input("Digite o seu ano de nascimento: "))
decisao = ano_nascimento(ano)
print(decisao)
