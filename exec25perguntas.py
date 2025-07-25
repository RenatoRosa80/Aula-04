"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre 
um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"
- 
O programa deve no final emitir uma classificação sobre a 
participação da pessoa no crime. Se a pessoa responder positivamente 
a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será 
classificado como "Inocente".

"""
print("Investigacao Criminal da Policia Civil!")
print(" Ao responder as questoes abaixo,\n saiba que tudo podera ser usado contra e ou a seu favor.")
print(" Responder TODAS as perguntas com S SIM ou N NAO. ")

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

# Contador de respostas positivas
respostas_positivas = 0

# Fazendo as perguntas
for pergunta in perguntas:
    resposta = str.lower(input(pergunta + " (s/n): "))
    if resposta == "s":
        respostas_positivas += 1

# Classificando a pessoa
if respostas_positivas == 2:
    classificacao = "Suspeita"
elif 3 <= respostas_positivas <= 4:
    classificacao = "Cúmplice"
elif respostas_positivas == 5:
    classificacao = "Assassino"
else:
    classificacao = "Inocente"

print("\nClassificação:", classificacao)






