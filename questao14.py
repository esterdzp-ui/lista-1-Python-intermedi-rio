# 14. O Clube dos Rebeldes (Validação Inversa): O clube secreto aceita todo mundo, exceto quem se chamar "Voldemort".
# Pergunte o nome e use o operador de diferença (!=) para barrar o vilão e liberar os outros.

nome = input("Digite seu nome: ")

if nome != "Voldemort":
    print("Bem‑vindo ao clube dos rebeldes!")
else:
    print("Você está barrado, Voldemort!")
