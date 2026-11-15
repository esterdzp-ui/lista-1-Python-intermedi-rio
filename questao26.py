# 26. O Radar de Velocidade: Pergunte a velocidade do carro (número).
# Se for menor ou igual a 100: "Siga em paz!".
# Se entre 100 e 200: "Multa gravíssima de 1000!".
# Se maior que 200: "Multa gravíssima de 2000 e carteira apreendida".

velocidade = float(input("Digite a velocidade do carro: "))

if velocidade <= 100:
    print("Siga em paz!")
elif velocidade > 100 and velocidade <= 200:
    print("Multa gravíssima de 1000!")
else:
    print("Multa gravíssima de 2000 e carteira apreendida")
