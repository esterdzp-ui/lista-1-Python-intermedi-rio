# 28. A Máquina do Tempo: Peça para o usuário digitar um ano.
# Se ano menor que 2000: "Você está no passado!".
# Se igual a 2026: "Você está no presente!".
# Se maior que 2026: "Você está no futuro!".

ano = int(input("Digite o ano: "))

if ano < 2000:
    print("Você está no passado!")
elif ano == 2026:
    print("Você está no presente!")
else:
    print("Você está no futuro!")
