# 2. Faça um Programa que peça um valor e mostre na tela se o valor 
# é positivo ou negativo.

# Solicita um valor ao usuário
valor = float(input("Digite um valor: "))

# Verifica se o valor é positivo, negativo ou zero
if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

"""
Explicação:
1. O programa usa input() para receber um valor do usuário, convertendo-o para float
2. Em seguida, verifica:
   - Se o valor for maior que 0, imprime "positivo"
   - Se for menor que 0, imprime "negativo"
   - Se for exatamente 0, imprime "zero"
3. O programa trata todos os casos possíveis de números reais
"""