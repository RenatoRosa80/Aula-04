"""
14. Faça um programa que lê as duas notas parciais obtidas por um
aluno numa disciplina ao longo de um semestre, e calcule a sua média.
A atribuição de conceitos obedece à tabela abaixo:

Média de Aproveitamento
- Entre 9.0 e 10.0 : A
- Entre 7.5 e 9.0 : B
- Entre 6.0 e 7.5 : C
- Entre 4.0 e 6.0 : D
- Entre 4.0 e zero : E

O algoritmo deve mostrar na tela as notas, a média, o conceito 
correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou 
“REPROVADO” se o conceito for D ou E.

"""
# Entrada

nota1 = float(input(" Informe a primeira nota obtida pelo Aluno: "))
nota2 = float(input(" Informe a segunda nota obtida pelo Aluno: "))
media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
    print(" A Média de Aproveitamento foi A! ")
    print(" Aprovado! Parabéns! ")
elif media >= 7.5 and media <= 9:
    print(" A Média de aproveitamento foi B! ")
    print(" Aprovado! Parabéns! ")
elif media >= 6 and media <= 7.5:
    print(" A Média de aproveitamento foi C! ")
    print(" Aprovado! Parabéns! ")

elif media >= 4 and media <= 6:
    print(" A Média de aproveitamento foi D! ")
    print(" Reprovado! Estude mais! ")
elif media >= 0 and media <= 4:
    print(" A Média de aproveitamento foi E! ")
    print(" Reprovado! Estude mais! ")
else:
    print(" Dados informados sao inválidos! ")
    