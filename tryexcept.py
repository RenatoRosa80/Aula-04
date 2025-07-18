"""
tryexcept

"""
numero = int(input(" Digite um número: "))
try:
    #print(" Deu bom... ")
    if( numero % 2 == 0) :
        print(" O número é PAR. ")
    else:
        print(" ÍMPAR. ")
except:
    print(" Deu ruim... ")


"""try:
    numero = int(input("Digite um número: "))
    
    if numero % 2 == 0:
        print("O número é PAR.")
    else:
        print("O número é ÍMPAR.")
except ValueError:
    print("Entrada inválida! Por favor, digite um número inteiro.")
    """
