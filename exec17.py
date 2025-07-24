"""
17. Faça um Programa que peça um número correspondente a um 
determinado ano e em seguida informe se este ano é ou não bissexto.

"""
#entrada
# Solicita ao usuário que informe um ano
ano = int(input("Digite um ano: "))

# Verifica se o ano é bissexto
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um Ano bissexto.")
else:
    print(f" {ano} não é um Ano bissexto.")
