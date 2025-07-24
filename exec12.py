"""
12. Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que depende do 
salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que 
o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao 
Salário Bruto menos os descontos. 

"""
"""
# ENTRADA:
O programa deverá pedir ao usuário o 
valor da sua hora e a quantidade de horas trabalhadas no mês.


# PROCESSAMENTO..:
- Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% Imprima na tela 
as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

  Salário Bruto: (5 * 220)        : R$ 1100,00
  (-) IR (5%)                     : R$   55,00  
  (-) INSS ( 10%)                 : R$  110,00
  FGTS (11%)                      : R$  121,00
  Total de descontos              : R$  165,00
  Salário Liquido                 : R$  935,00

"""

valor_hora_trabalhada = float(input(" Informe o valor da hora trabalhada:"))
qde_horas_trabalhadas_mes = int(input(" Quantas horas trabalhadas no mes? "))
salario_bruto = valor_hora_trabalhada * qde_horas_trabalhadas_mes
print(f" Salário Bruto => R$ {salario_bruto}")


if salario_bruto <= 900:
    irtexto = "Isento"
    print(" Salário isento de IR")
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - ( inss + fgts )
    print(f" O Salário Líquido é R$ {salario_liquido}")
    
    
elif salario_bruto >= 901 and salario_bruto <= 1500:
    irtexto = "5%" 
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - ( ir + inss + fgts )
    print(f" O Salário Líquido é R$ {salario_liquido}")
    print(f'(-) IR ({irtexto})                     : R$   {ir}')
    
elif salario_bruto >= 1501 and salario_bruto <= 2500:
    irtexto = "10%"
    ir = salario_bruto * 0.10
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - ( ir + inss + fgts )
    print(f" O Salário Líquido é R$ {salario_liquido}")
    print(f'(-) IR ({irtexto})                     : R$   {ir}')

else:
    irtexto = "20%"
    ir = salario_bruto * 0.20
    inss = salario_bruto * 0.10
    fgts = salario_bruto * 0.11
    salario_liquido = salario_bruto - ( ir + inss + fgts )
    print(f" O Salário Líquido é R$ {salario_liquido}")
    print(f'(-) IR ({irtexto})                     : R$   {ir}')

    