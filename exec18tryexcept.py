# 18. Faça um Programa que peça uma data no formato dd/mm/aaaa e 
# determine se a mesma é uma data válida.

from datetime import datetime

data = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    # Tenta converter a string para um objeto de data
    data_convertida = datetime.strptime(data, "%d/%m/%Y")
    print("A data é válida.")
except ValueError:
    print("Data inválida.")
