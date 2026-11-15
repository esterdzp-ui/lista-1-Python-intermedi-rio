# 21. O Chapéu Seletor Clássico: Pergunte: "Você prefere:1‑Livros, 2‑Esportes, 3‑Natureza, 4‑Pegadinhas?"
# Use if/elif/else para sortear o aluno em uma das 4 casas da escola de magia (ex: Corvinal, Grifinória, Lufa‑Lufa, Sonserina).

print("=== CHAPÉU SELETOR ===")
print("1‑Livros")
print("2‑Esportes")
print("3‑Natureza")
print("4‑Pegadinhas")

resposta = int(input("Digite o número da sua preferência: "))

if resposta == 1:
    casa = "Corvinal"
elif resposta == 2:
    casa = "Grifinória"
elif resposta == 3:
    casa = "Lufa‑Lufa"
elif resposta == 4:
    casa = "Sonserina"
else:
    casa = "Indefinida"

print(f" Você foi selecionado para a casa: {casa}")
