"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é 
imperdível. 

Confira:

Até 5 Kg:
- File Duplo R$ 4,90 por Kg
- Alcatra R$ 5,90 por Kg
- Picanha R$ 6,90 por Kg

Acima de 5 Kg:
- File Duplo R$ 5,80 por Kg
- Alcatra R$ 6,80 por Kg
- Picanha R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá 
levar apenas um dos tipos de carne da promoção, porém não há limites 
para a quantidade de carne por cliente. Se compra for feita no cartão 
Tabajara o cliente receberá ainda um desconto de 5% sobre o total da 
compra. Escreva um programa que peça o tipo e a quantidade de carne
comprada pelo usuário e gere um cupom fiscal, contendo as informações 
da compra: tipo e quantidade de carne, preço total, tipo de pagamento,
valor do desconto e valor a pagar.
"""
print(" Bem vindo ao Hipermercado Tabajaras!")
print ("-----------------------------------")
print(" Promocao do dia ")
print("------------------------------------")
print("Tipos de carne disponíveis:")
print("1 - Filé Duplo")
print("2 - Alcatra")
print("3 - Picanha")

tipo_carne = input("\nEscolha o tipo de carne (1/2/3): ")
quantidade = float(input("Informe a quantidade de carne (kg): "))
pagamento_cartao = str.lower(input("Pagamento com Cartão Tabajara? (s/n): "))

# Define os preços por tipo e quantidade
if tipo_carne == "1":
    nome_carne = "Filé Duplo"
    preco_kg = 4.90 if quantidade <= 5 else 5.80
elif tipo_carne == "2":
    nome_carne = "Alcatra"
    preco_kg = 5.90 if quantidade <= 5 else 6.80
elif tipo_carne == "3":
    nome_carne = "Picanha"
    preco_kg = 6.90 if quantidade <= 5 else 7.80
else:
    print("Tipo de carne inválido!")
    exit()

# Cálculo dos valores
preco_total = quantidade * preco_kg
desconto = preco_total * 0.05 if pagamento_cartao == "s" else 0
total_pagar = preco_total - desconto
tipo_pagamento = "Cartão Tabajara" if pagamento_cartao == "s" else "Dinheiro/Outro"

# Impressão do cupom fiscal
print("--------------------------------")
print("          CUPOM FISCAL          ")
print("--------------------------------")
print(f"Tipo de carne: {nome_carne}")
print(f"Quantidade: {quantidade:.2f} Kg")
print(f"Preço total: R$ {preco_total:.2f}")
print(f"Tipo de pagamento: {tipo_pagamento}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Valor a pagar: R$ {total_pagar:.2f}")
print("=========================")
