"""
27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg:
- Morango R$ 2,50 por Kg 
- Maçã R$ 1,80 por Kg

Acima de 5 Kg:
- Morango R$ 2,20 por Kg
- Maçã R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este 
total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos
e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser 
pago pelo cliente.

"""
print(" Bem vindo ao Hortifruti Sabor de Minas!")
morango = ()
maca = ()
qtde_morango = float(input(" Quantos kilos de Morango deseja? "))
qtde_maca = float(input(" Quantos kilos de maca deseja? "))
qtde_total_de_frutas = (qtde_morango + qtde_maca)
valor_compra_desconto =()
valor_total_compra = ()
valor_desconto = ()
valor_morango = ()
valor_maca = ()

if qtde_total_de_frutas > 0 and qtde_total_de_frutas <= 5 :
    morango = 2.50
    maca = 1.80
    morangotexto = "2.50"
    macatexto = "1.80"
    print(f'(-) Kg do Morango                      : R$   {2.50}')
    print(f'(-) Kg da Maca                    : R$   {1.80}')

    valor_morango = morango * qtde_morango
    print(f" Valor Morango a pagar: R$ {valor_morango:.2f}")
    valor_maca = maca * qtde_maca
    print(f" Valor Maca a pagar : R$ {valor_maca:.2f}")
    valor_total_compra = valor_morango + valor_maca
    print(f"Valor final a pagar: R$ {valor_total_compra:.2f}" )
    print(" Obrigado e volte sempre! ")

elif qtde_total_de_frutas > 5 and qtde_total_de_frutas <= 8:
    morango = 2.20
    maca = 1.50
    print(f'(-) Kg do Morango                      : R$   {2.20}')
    print(f'(-) Kg da Maca                    : R$   {1.50}')
    valor_morango = morango * qtde_morango
    print(f" Valor Morango a pagar: R$ {valor_morango:.2f}")
    valor_maca = maca * qtde_maca
    print(f" Valor Maca a pagar : R$ {valor_maca:.2f}")
    #qtde_total_de_frutas = morango + maca
    valor_total_compra= valor_morango + valor_maca
    print(f" Valor final a pagar: R$ {valor_total_compra:.2f} ")
    print(" Obrigado e volte sempre! ")

elif qtde_total_de_frutas > 8 or valor_total_compra > 25.00:
    morango = 2.20
    maca = 1.50
    print(f'(-) Kg do Morango                      : R$   {2.20}')
    print(f'(-) Kg da Maca                    : R$   {1.50}')
    valor_morango = morango * qtde_morango
    print(f" Valor Morango a pagar: R$ {valor_morango:.2f}")
    valor_maca = maca * qtde_maca
    valor_total_compra= valor_morango + valor_maca
    valor_compra_desconto = valor_total_compra * 0.10
    print(f" Desconte de R$: {valor_compra_desconto:.2f} ")
    valor_desconto = valor_total_compra - valor_compra_desconto
    print(f" Valor a Pagar: R$ {valor_desconto:.2f} ")
    print(" Obrigado e volte sempre! ")
else:
    print(" Dados incorretos! ")
    
     
    
