# 1. Faça um Programa que peça dois números e imprima o maior deles.

num1 = int(input(" digite um número inteiro: "))
num2 = int(input(" Digite um segundo número inteiro: "))

if num1 > num2 and num1 != num2 : 
    print(" Número 1 é maior! ")
elif num1 < num2 and num2 != num1 :
    print(" Número 2 é maior! " )
else:
    print(" Os números sao iguais!")

