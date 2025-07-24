# 6. Faça um Programa que leia três números e mostre o maior deles.

#Entrada

num1 = float(input(" Informe o primeiro número: "))
num2 = float(input(" Informe o segundo número: "))
num3 = float(input(" Informe o terceiro número: "))

# Processamento
if num1 > num2 and num1 > num3:
    print(" O primeiro número é o maior de todos! ")
elif num2 > num1 and num2 > num3:
    print(" O segundo número é o maior de todos! ")
elif num3 > num1 and num3 > num2:
    print(" O terceiro número é o maior de todos!")
elif num1 == num2 and num1 == num3:
    print(" Todos os números digitados sao iguais! ")
elif num2 == num1 and num2 == num3:
    print(" Todos os números digitados sao iguais! ")
elif num3 == num1 and num3 == num2:
    print(" Todos os números digitados sao iguais!")
else:
    print(" Dados digitados nao aceitaveis!")