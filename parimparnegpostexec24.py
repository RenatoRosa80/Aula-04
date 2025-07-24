"""
24. Faça um Programa que leia 2 números e em seguida pergunte ao 
usuário qual operação ele deseja realizar. O resultado da 
operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;(% 2 == 0)

- positivo ou negativo; (>=0 <0)

- inteiro ou decimal. (.is_integer)

"""
print("Bem vindo ao Sistema de calculo!\n O sistema disponibiliza as seguintes operacoes: ")
print("SOMA; SUBTRACAO; MULTIPLICACAO E DIVISAO")
operacao = str.lower(input(" Qual operacao deseja fazer? "))

num1 = (float(input(" informe o primeiro número: ")))
num2 = (float(input(" informe o segundo número: ")))



if operacao == "soma":
    operacao_soma = num1 + num2  
    print(f" O resultado é: {operacao_soma:.2f}")
    if operacao_soma % 2 == 0:
        print("O número é PAR! " )
    else:
        print(" O número é IMPAR! ")
    if operacao_soma >=0 :
        print("O número é POSITIVO! " )
    else:
        print(" O número é NEGATIVO! ")
    if operacao_soma.is_integer() :
        print("O número é INTEIRO! " )
    else:
        print(" O número é DECIMAL! ")
    
elif operacao == "subtracao":
    operacao_sub = num1 - num2  
    print(f" O resultado é: {operacao_sub:.2f}")
    if operacao_sub % 2 == 0:
        print("O número é PAR! " )
    else:
        print(" O número é IMPAR! ")
    if operacao_sub >=0 :
        print("O número é POSITIVO! " )
    else:
        print(" O número é NEGATIVO! ")
    if operacao_sub.is_integer() :
        print("O número é INTEIRO! " )
    else:
        print(" O número é DECIMAL! ")
elif operacao == "multiplicacao":
    operacao_mult = num1 * num2  
    print(f" O resultado é: {operacao_mult:.2f}")
    if operacao_mult % 2 == 0:
        print("O número é PAR! " )
    else:
        print(" O número é IMPAR! ")
    if operacao_mult >=0 :
        print("O número é POSITIVO! " )
    else:
        print(" O número é NEGATIVO! ")
    if operacao_mult.is_integer() :
        print("O número é INTEIRO! " )
    else:
        print(" O número é DECIMAL! ")
elif operacao == "divisao":
    operacao_div = num1 / num2  
    print(f" O resultado é: {operacao_div:.2f}")
    if operacao_div % 2 == 0:
        print("O número é PAR! " )
    else:
        print(" O número é IMPAR! ")
    if operacao_div >=0 :
        print("O número é POSITIVO! " )
    else:
        print(" O número é NEGATIVO! ")
    if operacao_div.is_integer() :
        print("O número é INTEIRO! " )
    else:
        print(" O número é DECIMAL! ")
else:
    print(" Dados informados sao inconsistenzes! ")
    