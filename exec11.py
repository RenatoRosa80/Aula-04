"""
11. As Organizações Tabajara resolveram dar um aumento de salário aos 
seus colaboradores e lhe contraram para desenvolver o programa que 
calculará os reajustes.

Faça um programa que recebe o salário de um colaborador e o reajuste 
segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento 
ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.

"""
salario = float(input(" Informe o seu Salário: "))



if salario <= 280:
    salario_novo1 = salario * 0.20
    salario_reajustado = salario + salario_novo1
    valor_aumento = salario_reajustado - salario 
    
    print (f" O salario anterior é {salario:}")
    print (f"O salário reajustado é de R$ {salario_reajustado:}")
    print(f" O valor do aumento foi de R$ {valor_aumento:}")
    print(" o salário foi reajustado em 20% ")

    
elif salario >=  281 and salario <= 700:
    salario_novo2  = salario * 0.15
    salario_reajustado = salario + salario_novo2
    valor_aumento = salario_reajustado - salario
   
 
    print(f" O Salário reajustado é de R$ {salario_reajustado:}")
    print (f" O salario anterior é {salario:}")
    print(f" O valor do aumento foi de R$ {valor_aumento:}")
    print(" o salário foi reajustado em 15% ")
    
elif salario > 700:
    salario_novo3  = salario * 0.05
    salario_reajustado = salario + salario_novo3
    valor_aumento = salario_reajustado - salario
   

    print(f" O Salário reajustado é de R$ {salario_reajustado:}")
    print (f" O salario anterior é {salario:}")
    print(f" O valor do aumento foi de R$ {valor_aumento:}")
    print(" o salário foi reajustado em 5% ")

    
else:
    print(" Dados informados sâo incorretos! ")