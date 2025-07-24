"""
20. Faça um Programa para leitura de três notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e presentar:
- A mensagem "Aprovado", se a média for maior ou igual a 7, com a 
respectiva média alcançada;
- A mensagem "Reprovado", se a média for menor do que 7, 
com a respectiva média alcançada;
- A mensagem "Aprovado com Distinção", se a média for igual a 10.

"""
#ENTRADA

nota1 = float(input(" Informe a primeira nota parcial: "))
nota2 = float(input(" Informe a segunda nota parcial: "))
nota3 = float(input(" Informe a terceira nota parcial: "))

#PROCESSAMENTO
media = (nota1 + nota2 + nota3) / 3

if media >= 7 and media <= 9.99:
    print(f" A media obtida foi {media:.2f}")
    print(" APROVADO! ")
elif media <=6.9:
    print(f" A media obtida foi {media:.2f}")
    print(" REPROVADO! ")
elif media == 10:
    print(f" A media obtida foi {media:.2f}")
    print(" APROVADO COM DISTINCAO! ")
else:
    print(" Dados digitados incorretos! ")