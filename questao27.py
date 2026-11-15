# 27. O Sistema Escolar (Calculadora de Notas): Peça as notas de duas provas.
# Calcule a média. Se média >= 7: Aprovado. Se >= 5 e < 7: Recuperação.
# Se média < 5: Reprovado.

nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))

media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Média: {media:.2f} — Aprovado")
elif media >= 5:
    print(f"Média: {media:.2f} — Recuperação")
else:
    print(f"Média: {media:.2f} — Reprovado")
