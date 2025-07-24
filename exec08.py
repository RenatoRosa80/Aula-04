"""
8. Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato.
"""

#Entrada

preco_produto1 = float(input( " Informe o valor do produto 1: "))

preco_produto2 = float(input( " Informe o valor do produto 2: "))

preco_produto3 = float(input( " Informe o valor do produto 3: "))
"""print(preco_produto1)
print(preco_produto2)
print(preco_produto3)
"""

if preco_produto1 < preco_produto2 and preco_produto1 < preco_produto3:
   print(" Voce deve comprar o produto 1, pois é mais barato!")
   print(f"O valor do produto 1 é $ {preco_produto1:}")
elif preco_produto2 < preco_produto3 and preco_produto2 < preco_produto1:
   print(" Voce deve comprar o produto 2, pois é o mais barato!") 
   print(f"O valor do produto 2 é $ {preco_produto2:}")
elif preco_produto3 < preco_produto2 and preco_produto3 < preco_produto1:
   print(" Voce deve comprar o produto 3, pois é o mais barato!")
   print(f"O valor do produto 3 é $ {preco_produto3:}")
else:
    print(" Preços são todos iguais! ")