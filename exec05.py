# 5. Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
"""

- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.

"""
# Entrada

nota1 = float(input(" Informe a primeira nota obtida pelo Aluno: "))
nota2 = float(input(" Informe a segunda nota obtida pelo aluno: "))
media = (nota1 + nota2) / 2

# processamento

if media = 10:
    print(f" Aprovado com excelencia com média de {media:.2f} ! ")
elif media >= 7:
    print(f" Aprovado com media de {media:.2f}  ! ")
else:
    print(f" Reprovado! Sua média foi {media:.2f}.  ")