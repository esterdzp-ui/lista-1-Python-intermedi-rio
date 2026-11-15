# 30. DESAFIO FINAL: A Taverna do Dragão
# Passo 1: Pede senha secreta para entrar. Errou → programa acaba.
# Passo 2: Se acertou, pede idade. Menor de 13 → sai. Maior/igual 13 continua.
# Passo 3: Taverneiro pergunta personalidade, escolhe item de sorteio.
# Passo 4: Calculadora de mesada para ver se tem dinheiro para comprar o item sorteado.

# PASSO 1
senha = input("Digite a senha secreta para entrar na Taverna: ")
if senha != "dragao123":
    print("Senha errada! Você foi expulso da Taverna.")

else:
    # PASSO 2
    idade = int(input("Digite sua idade: "))
    if idade < 13:
        print("Idade insuficiente para ficar na Taverna. Saia!")

    else:
        # PASSO 3
        print("Escolha sua personalidade:")
        print("1‑Corajoso")
        print("2‑Cauteloso")
        escolha = int(input("Digite 1 ou 2: "))

        if escolha == 1:
            preco_item = 30
            nome_item = "Espada Mágica"
        elif escolha == 2:
            preco_item = 20
            nome_item = "Poção de Cura"
        else:
            preco_item = 0
            nome_item = "Nenhum item"

        # PASSO 4
        if preco_item != 0:
            mesada = float(input(f"O item sorteado é {nome_item}, custa R${preco_item}. Digite quanto você tem de mesada: "))
            if mesada >= preco_item:
                troco = mesada - preco_item
                print(f"Compra aprovada! Você levou {nome_item}. Troco R${troco:.2f}")
            else:
                print(f"Falta dinheiro para comprar {nome_item}")
        else:
            print("Escolha de personalidade inválida")


