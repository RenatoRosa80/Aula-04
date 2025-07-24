# 4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input( " Informe uma Vogal ou Consoante: ")
letra = letra.lower()
if letra.isalpha():
    if letra == "a":
        print(" É uma Vogal. ")
    elif letra == "e":
        print(" É uma Vogal. ")
    elif letra == "i":
        print(" É uma Vogal. ")
    elif letra == "o":
        print(" É uma Vogal. ")
    elif letra == "u":
        print(" É uma Vogal! ")
        print(" insira uma letra ou Consoante: ")
    else:
        print(" É uma Consoante! ")
else:
    print(" O dado digitado nao é aceitado, Digite uma Vogal ou Consoante!")