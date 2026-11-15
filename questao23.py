# 23. Seletor de Classes RPG: Faça duas perguntas.
# 1‑Prefere atacar de longe (1) ou de perto (2)?
# Dentro do primeiro if (longe), pergunte "Magia (A) ou Arco (B)?" para definir Mago ou Arqueiro.
# Dentro do else (perto), pergunte "Espada (A) ou Adagas (B)?" para definir Guerreiro ou Assassino. (Lógica de If aninhado).

pergunta1 = int(input("Prefere atacar de longe (1) ou de perto (2)? "))

if pergunta1 == 1:
    pergunta2 = input("Longe: Magia (A) ou Arco (B)? ").upper()
    if pergunta2 == "A":
        classe = "Mago"
    elif pergunta2 == "B":
        classe = "Arqueiro"
    else:
        classe = "Inválido"
else:
    pergunta2 = input("Perto: Espada (A) ou Adagas (B)? ").upper()
    if pergunta2 == "A":
        classe = "Guerreiro"
    elif pergunta2 == "B":
        classe = "Assassino"
    else:
        classe = "Inválido"

print(f" Sua classe de RPG é: {classe}")
