# 25. O Guru dos Animais: Pergunte a idade e se ele prefere gatos ou cachorros.
# Crie 4 respostas possíveis combinando os dados (Ex: "Jovem e prefere gatos", "Adulto e prefere cachorros", etc).

idade = int(input("Digite sua idade: "))
animal = input("Prefere gatos ou cachorros? ").lower()

if idade < 18:
    if animal == "gatos":
        frase = "Jovem e prefere gatos"
    elif animal == "cachorros":
        frase = "Jovem e prefere cachorros"
    else:
        frase = "Animal inválido"
else:
    if animal == "gatos":
        frase = "Adulto e prefere gatos"
    elif animal == "cachorros":
        frase = "Adulto e prefere cachorros"
    else:
        frase = "Animal inválido"

print(frase)
