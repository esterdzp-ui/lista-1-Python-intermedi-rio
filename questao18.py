# 18. Imposto do Reino: Peça o valor do tesouro do herói.
# Se o tesouro for maior que 1000 moedas, ele recebe uma taxa de 10% de desconto.
# Se for menor ou igual a 1000, herói não paga imposto.

tesouro = float(input("Digite quantas moedas tem no tesouro: "))

if tesouro > 1000:
    desconto = tesouro * 0.10
    total = tesouro - desconto
    print(f"Desconto de 10% aplicado! Valor final: {total:.2f} moedas")
else:
    print(f"Sem imposto! Valor mantido: {tesouro:.2f} moedas")

