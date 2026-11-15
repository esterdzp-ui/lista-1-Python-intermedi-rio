# 19. Caixa Eletrônico da Mesada: O pai deu a mesada, mas perguntou: "Você tirou nota A em matemática?".
# Se a resposta for "sim", a mesada recebe um bônus de 20 moedas. Se for "não", recebe apenas o valor normal.

mesada = float(input("Digite o valor normal da mesada: "))
notaA = input("Você tirou nota A em matemática? (sim / não): ").lower()

if notaA == "sim":
    total = mesada + 20
else:
    total = mesada

print(f"Total final da mesada: R${total:.2f}")
