nomeP = input("Digite o seu nome próprio: ")
nomeF = input("Digite o seu ultimo nome: ")
print("Olá", nomeP + " " + nomeF, "o seu registo está criado")

nomeP_email = nomeP[0].lower()
nomeF_email = nomeF.lower()
nome_final = nomeP_email+"."+nomeF_email+"."+"edu@empresa.pt"
print("O seu email é ", nome_final)
