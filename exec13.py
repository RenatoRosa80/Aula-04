"""
13. Faça um Programa que leia um número e exiba o dia 
correspondente da semana. (1-Domingo, 2- Segunda, etc.), 
se digitar outro valor deve aparecer valor inválido.
"""

#ENTRADA

dia_semana = int(input(" Digize um número de 1 a 7:  "))

if dia_semana == 1:
    print(" Hoje é Domingo!")
elif dia_semana == 2:
    print(" Hoje é Segunda feira! ")
elif dia_semana == 3:
    print(" Hoje é Terca feira! ")
elif dia_semana == 4:
    print(" Hoje é Quarta feira!  ")
elif dia_semana == 5:
    print(" Hoje é Quinta feira! ")
elif dia_semana == 6:
    print(" Hoje é Sexta feira! ") 
elif dia_semana == 7:
    print(" Hoje é Süabado! ")
else:
    print(" Valor digitado é inválido. Tente novamente! ")
