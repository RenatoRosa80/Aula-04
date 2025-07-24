# 3. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#Entrada
sexo = str(input(" Informe o sexo, F - Feminino ou M - Masculino: "))
sexo = sexo.lower()

if sexo == "F":
    print(" Feminino ")
else:
    print(" Masculino ")
