# 20. A Cantina Inflacionada: Usuário informa o dinheiro que tem e escolhe Lanche (R$15), Suco (R$8) ou Combo (R$20).
# Use elif para identificar a escolha, verificar se tem dinheiro para pagar, liberar ou negar a venda.

print("=== CANTINA ===")
print("1‑Lanche R$15,00")
print("2‑Suco R$8,00")
print("3‑Combo R$20,00")

dinheiro = float(input("Quanto dinheiro você tem? R$"))
pedido = int(input("Digite 1‑Lanche / 2‑Suco / 3‑Combo: "))

if pedido == 1:
    preco = 15
elif pedido == 2:
    preco = 8
elif pedido == 3:
    preco = 20
else:
    preco = 0
    print("Pedido inválido")

if preco != 0:
    if dinheiro >= preco:
        troco = dinheiro - preco
        print(f"Venda liberada! Troco: R${troco:.2f}")
    else:
        print("Dinheiro insuficiente, venda negada")
