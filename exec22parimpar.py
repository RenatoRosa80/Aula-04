#22. Faça um Programa que peça um número inteiro 
# e determine se ele é par ou impar. Dica: utilize o operador módulo
# (resto da divisão).

num = int(input(" Informe um número inteiro: "))

if (num % 2 == 0) :
    print( " O número informado eh PAR! ")
else:
    print(" O número informado eh IMPAR! ")