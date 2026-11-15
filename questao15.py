# 15. A Senha Sensível (Caps Lock): Peça a senha secreta. Adicione um elif para testar se o usuário digitou a senha certa, mas toda em MAIÚSCULAS,
# e imprima um aviso: "Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas."

senha_correta = "senha123"
digitado = input("Digite a senha secreta: ")

if digitado == senha_correta:
    print("Senha correta! Acesso liberado.")
elif digitado == senha_correta.upper():
    print("Quase! Mas você gritou a senha (Caps Lock). Tente minúsculas.")
else:
    print("Senha errada, tente novamente.")
