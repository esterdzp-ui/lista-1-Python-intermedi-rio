# 17. A Feira de Poções Múltiplos Produtos: Mostre um menu com 3 poções e preços diferentes.
# Peça para o usuário digitar 1, 2 ou 3. Use if/elif/else para calcular o valor da compra baseado na escolha.

print("=== MENU POÇÕES ===")
print("1‑Poção de Cura R$12,00")
print("2‑Poção de Força R$18,00")
print("3‑Poção de Velocidade R$15,00")

escolha = int(input("Digite 1, 2 ou 3 para escolher sua poção: "))

if escolha == 1:
    valor = 12
elif escolha == 2:
    valor = 18
elif escolha == 3:
    valor = 15
else:
    valor = 0
    print("Escolha inválida!")

if valor != 0:
    print(f"Total da compra: R${valor:.2f}")
