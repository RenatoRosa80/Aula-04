"""15. Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo. 
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero,
isósceles ou escaleno. 
"""

"""
Dicas:

- Três lados formam um triângulo quando a soma de quaisquer dois lados
for maior que o terceiro;
- Triângulo Equilátero: três lados iguais;
- Triângulo Isósceles: quaisquer dois lados iguais;
- Triângulo Escaleno: três lados diferentes;

"""

#ENTRADA

lado1 = float(input(" Informe a medida do 1° lado do Triangulo: "))
lado2 = float(input(" Informe a medida do 2° lado do Triangulo: "))
lado3 = float(input(" Informe a medida do 3° lado do Triangulo: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2)  and (lado2 + lado3> lado1) :
    print(" E um Triangulo! ")
    if lado1 == lado2 == lado3 : 
        print(" E um Triângulo Equilátero! ")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3 :
        print(" E um Triângulo Isósceles! ")
    else:
        print(" E um Triângulo Escaleno! ")
else :
    print(" Os lados nao formam um Triangulo!! ")