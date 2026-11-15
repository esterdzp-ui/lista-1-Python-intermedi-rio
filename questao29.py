# 29. O Enigma da Esfinge: Faça uma conta matemática surpresa (ex: 15 * 3).
# Peça o valor usando input. Se acertar, ganha o tesouro. Senão, perde 50 de vida.

resposta_correta = 45
chute = int(input("Quanto é 15 multiplicado por 3? "))

if chute == resposta_correta:
    print("Parabéns! Você ganhou o tesouro")
else:
    print("Errou! Perdeu 50 pontos de vida")

