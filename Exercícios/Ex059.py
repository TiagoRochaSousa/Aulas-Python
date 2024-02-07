#Exercicio59

def mensagem(msg):
    print(f"*" * len(msg))
    print(f"{msg:^30}")
    print(f"*" * len(msg))

mensagem("Olá mundo")
mensagem("VAmos ver esta mensagem grande")
mensagem("Agora esta mais pequena")
