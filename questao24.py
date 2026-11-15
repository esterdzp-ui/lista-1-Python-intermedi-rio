# 24. O Termômetro de Humor: Pergunte ao usuário uma cor (Azul, Amarelo, Vermelho).
# O sistema deve responder como ele está se sentindo usando elif (Ex: Azul = Calmo, Vermelho = Zangado).

cor = input("Escolha uma cor: Azul / Amarelo / Vermelho: ").capitalize()

if cor == "Azul":
    humor = " Calmo"
elif cor == "Amarelo":
    humor = " Feliz"
elif cor == "Vermelho":
    humor = " Zangado"
else:
    humor = " Não consegui identificar seu humor"

print(f"Seu humor: {humor}")
