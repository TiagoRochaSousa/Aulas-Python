#Exercicio42

jogos = ("Nioh - Playstation Hits PS4", 19.99,
         "Marvel's Spider-Man: Miles Morales PS2", 59.99,
         "Baldur's Gate 3", 59.99,
         "Elden Ring", 35.99,
         "Cyberpunk 77", 29.99,
         "Hogwarts Legacy", 25.99,
         "Red Dead Redemption 2", 19.79)

for pos in range(0, len(jogos)):
    if pos % 2 == 0:
        print(f"{jogos [pos]:-<45}", end="")
    else:
        print(f"{jogos[pos]:<7.2f}€")
