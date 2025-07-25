"""
26. Um posto está vendendo combustíveis com a seguinte tabela de 
descontos: 

Álcool:
- até 20 litros, desconto de 3% por litro
- acima de 20 litros, desconto de 5% por litro 

Gasolina:
- até 20 litros, desconto de 4% por litro
- acima de 20 litros, desconto de 6% por litro 

Escreva um algoritmo que leia o número de litros vendidos, 
o tipo de combustível (codificado da seguinte forma: A-álcool,
G-gasolina), calcule e imprima o valor a ser pago pelo cliente 
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do 
litro do álcool é R$ 1,90.

"""

print(" Bem vindos ao Posto de Combustivel Tabajaras ")
print(" Tabela de promocao: ")
print("Álcool:\n- até 20 litros, desconto de 3% por litro\n- acima de 20 litros, desconto de 5% por litro ")
print("Gasolina:\n- até 20 litros, desconto de 4% por litro\n- acima de 20 litros, desconto de 6% por litro ")
print("--------------------------------------------------------")
alcool_litro = 1.90

gasolina_litro = 2.50 
#desconto = ()
#total_a_pagar = ()

tipo_combustivel = str.upper(input(" Deseja abastecer com Alcool - A ou Gasolina - G? "))
litros = float(input(" Quantos litros deseja abastecer? "))

if tipo_combustivel == "A":
    if litros <= 20:
        total_a_pagar = alcool_litro * litros
        print(f" Valor sem desconto: R$ {total_a_pagar:.2f}")
        desconto = total_a_pagar * 0.03
        print(f"Desconto de R$ {desconto}")
        valor_com_desconto = total_a_pagar - desconto
        print("--------------------------------------------------------")
        print(f" Valor final a pagar R$ {valor_com_desconto:.2f}")
        print("--------------------------------------------------------")
        print(" Obrigado e volte sempre! ")
    elif litros > 20:
        total_a_pagar = alcool_litro * litros
        print(f"{total_a_pagar}")
        desconto = total_a_pagar * 0.05
        print(f"Desconto de R$ {desconto}")
        valor_com_desconto = total_a_pagar - desconto
        print("--------------------------------------------------------")
        print(f" Valor final a pagar R$ {valor_com_desconto:.2f}")
        print("--------------------------------------------------------")
        print(" Obrigado e volte sempre! ")
    else:
        print("Dados incorretos")

        
elif tipo_combustivel == "G":
    if litros <= 20:
        gasolina_litro = 2.50 
        total_a_pagar = gasolina_litro * litros 
        print(f" Valor sem desconto: R$ {total_a_pagar}")
        desconto = total_a_pagar * 0.05
        print(f"Desconto de R$ {desconto}")
        valor_com_desconto = total_a_pagar - desconto
        print("--------------------------------------------------------")
        print(f" Valor final a pagar R$ {valor_com_desconto:.2f}")
        print("--------------------------------------------------------")
        print(" Obrigado e volte sempre! ")
    elif litros > 20 :
        gasolina_litro = 2.50 
        total_a_pagar = gasolina_litro * litros 
        print(f"Valor sem desconto: R$ {total_a_pagar}")
        desconto = total_a_pagar * 0.06
        print(f"Desconto de R$  {desconto}")
        valor_com_desconto = total_a_pagar - desconto
        print("--------------------------------------------------------")
        print(f" Valor final a pagar R$ {valor_com_desconto:.2f}")
        print("--------------------------------------------------------")
        print(" Obrigado e volte sempre! ")
    else:
        print(" Digitos invalidos! ") 
else:
    print(" Dados incorretos! ")


       
    
    

