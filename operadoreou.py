"""
Temos duas condições ( dinheiro e senha) o que nos da 4 condições ( 2² = 4 ).
"""

dinheiro = False
senha = False

if dinheiro == True and senha == True:
#if dinheiro == True and senha == True: 
    print(" Sacar ")
elif dinheiro == True and senha == False:
    print(" Senha inválida! ")
elif dinheiro == False and senha == True:
    print(" Saldo Insuficiente! " )
elif dinheiro == False and senha == False:
    print(" Dados incorretos.")
