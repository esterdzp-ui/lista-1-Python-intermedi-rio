# 22. O Bug do Chapéu: Melhore o exercício anterior.
# Adicione um else poderoso no final para caso o usuário digitar "5" ou qualquer letra errada,
# fazendo o chapéu responder: "Hmm, escolha inválida. O Chapéu está confuso!".

print("=== CHAPÉU SELETOR V2 ===")
print("1‑Livros")
print("2‑Esportes")
print("3‑Natureza")
print("4‑Pegadinhas")

resposta = input("Digite o número da sua preferência: ")

if resposta == "1":
    casa = "Corvinal"
elif resposta == "2":
    casa = "Grifinória"
elif resposta == "3":
    casa = "Lufa‑Lufa"
elif resposta == "4":
    casa = "Sonserina"
else:
    casa = "inválido"

if casa == "inválido":
    print("Hmm, escolha inválida. O Chapéu está confuso!")
else:
    print(f"Você foi selecionado para a casa: {casa}")
