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