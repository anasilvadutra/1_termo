# Exercícios de Programação Python: "O Caça-Erros"
# Errado
# 1. O Problema da Idade
# idade = input("Digite sua idade: ")
# if idade >= 18:
# print("Você é maior de idade.")

# Corrigido
# idade = int(input("Digite sua idade:  "))
# if idade >= 18:
#     print("Você é maior de idade.")

# Melhorado
# idade = int(input("Digite a sua idade:  "))
# if idade >= 18:
#     print("Você é maior de idade")
# elif idade <= 18:
#     print("Você é menor de idade!")

# 2. A Escrita Fiel
# Errado
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# Corrigido
# nome = "Mariana"
# print(f"Seja bem-vinda, {nome}!")

# Melhorada
# nome = input("Qual seu nome? ")
# print(f"Seja bem-vinda {nome}!")

# 3. Falta de Espaço
# Errado
# numero = 10
# if numero > 5:
# print("O número é maior que cinco.")
# else:
# print("O número é menor ou igual a cinco.")

# Corrigido
# numero = 10
# if numero >= 5:
#     print("O numero é maior que cinco.")
# else:
#     print("O numero é maior que cinco")

# Melhorado
# numero = int(input("Fale um numero de 0 a 10 "))
# if numero >= 5:
#     print("O numero é maior que cinco.")
# elif numero <= 5:
#     print("O numero e menor que cinco")

# 4. Esquecimento Fatal
# Errada
# usuario = "aluno123"
# if usuario == "aluno123"
# print("Login realizado com sucesso.")

# Corrigido
# usuario = "aluno123"
# if usuario == "aluno123":
#     print("Login realizado com sucesso")

# Melhorado
# usuario = ("aluno123")
# if usuario == "aluno123":
#     print("Login do aluno realizado com sucesso! ")

# 5. Atribuição vs. Comparação
# Errada
# clima = "ensolarado"
# if clima = "chuvoso":
# print("Leve um guarda-chuva!")

# Corrigido
# clima = "Ensolarado"
# if clima == "chuvoso":
#     print("Leve um guarda-guva!")

# Melhorado
# clima = input("O clima de hoje esta chuvoso? sim/nao  ")
# if clima == "sim":
#     print("Leve um guarda-chuva!")
# elif clima == "nao":
#     print("Não precisa levar guarda-chuva ")
# else:
#     print("Erro na temperatura")

# 6. Misturando Alhos com Bugalhos
# Errada
# pontos = 50
# print("Parabéns! Você fez " + pontos + " pontos.")

# Corrigido
# pontos = 50
# print(f" Parabens! Você fez {pontos} pontos.")

# Melhorada
# pontos = int(input("Quantos pontos você fez?"))
# if pontos <= 40:
#     print("Você ficou abaixo da pontuação adeguada")
# elif pontos >= 50:
#     print("Você ficou com boa pontuação, continue assim!")
# else:
#     print("Erro na pontuação!")

# 7. A Ordem dos Fatores
# Errado
# O sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >= 7:
# print("Aprovado")
# elif nota >= 9:
# print("Excelente!")

# Corrigido
# nota = 9.5
# if nota >= 9:
#     print("Excelente!")
# elif nota >= 7:
#     print("Aprovado") 

# Melhorado
# int(input("Qual foi sua nota de 0 a 10? "))
# nota = 9.5
# if nota >= 9:
#     print("Excelente!")
# elif nota <= 5 :
#     print("Aprovado")
# else:
#     ("Erro nas notas")

# 8. O Contador de 1 a 5
# Errado
# for i in range(5):
# print(i)

