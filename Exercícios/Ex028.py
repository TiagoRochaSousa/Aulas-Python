#Exercicio28
resposta = ""

while resposta != "V" or "F":
    print("A terra é plana?")
    resposta = input("---> ").upper()
    if resposta == "V":
        print("A resposta está errada")
        break
    elif resposta == "F":
        print("A resposta está certa")
        break
    else:
        print("A sua resposta nao esta bem formatada digite novamente:")
while resposta != "V" or "F":
    print("A lua gira em torno da Terra?")
    resposta = input("---> ").upper()
    if resposta == "V":
        print("A resposta está certa")
        break
    elif resposta == "F":
        print("A resposta está errada")
        break
    else:
        print("A sua resposta nao esta bem formatada digite novamente:")
while resposta != "V" or "F":
    print("A Terra gira em torno do Sol?")
    resposta = input("---> ").upper()
    if resposta == "V":
        print("A resposta está certa")
        break
    elif resposta == "F":
        print("A resposta está errada")
        break
    else:
        print("A sua resposta nao esta bem formatada digite novamente:")
