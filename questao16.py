# 16. O Jogo Novo: Pergunte o valor da mesada guardada e o preço de um jogo que o aluno quer.
# Se o valor for suficiente, calcule e mostre o troco. Senão, diga exatamente quanto dinheiro falta.

mesada = float(input("Quanto você tem guardado de mesada? R$"))
preco_jogo = float(input("Quanto custa o jogo? R$"))

if mesada >= preco_jogo:
    troco = mesada - preco_jogo
    print(f"Você consegue comprar! O troco será de R${troco:.2f}")
else:
    falta = preco_jogo - mesada
    print(f"Falta R${falta:.2f} para comprar o jogo!")
