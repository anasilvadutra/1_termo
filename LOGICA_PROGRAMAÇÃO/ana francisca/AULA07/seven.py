# Clean code - Aula 7
# para que usar? 
# como usar?
# print("Clean code - Aula 7")
# aula = 7
# print(f"Estamos na aula {aula} de Clean Code")

# print("Perfil de Game")
# nick=input("Qual seu nome? ")
# nivel=int(input("Qual o seu nível no jogo? "))
# print(f"O jogador {nick} está no nível {nivel} e pronto para a partida!")

# print("Calculadora De Mesada")
# semana= int(input("Qual o valor que você recebe por semana? "))
# final_do_mes= semana*4
# print(f"No final do mês você terá uma mesada de: {final_do_mes}")

# Manipulação de arquivos e Texto
# TEXTO = " Python é Muito legal! "
# print(TEXTO.strip().upper()) # "PYTHON"
# print(TEXTO.strip().lower()) # "python"
# print(TEXTO.strip().startswith("A")) # "Começar com Letra Inicial"
# print(TEXTO.strip().capitalize()) # "Letras Inicial"
# print(TEXTO.strip().title()) # "Titulo"
# print(TEXTO.strip().replace("_","_")) # "Preencher vazios"
# print(TEXTO.strip().split()) # " Separar palavras"

# Exercicio 1:
# Crie um programa que peça ao úsuario para inserir uma frase e, em seguida , exiba a frase com seguintes transformações: 
# - Deixe o texto em letras minusculas

# frase=input("Digite uma frase: ")
# print(frase.strip().lower())

# Manipular arquivos:
# Escrevendo
# with open("notas.txt","w", encoding="utf-8") as textos:
#     textos.write("Estudar Python hoje!")
#     textos.write("\nLer sobre Clean Code.")
#     textos.write("\n Estamos evoluindo.")

# # lendo
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo= texto.read()
#     print(conteudo)

# Exemplo 1:
# Crie um programa que leia o conteudo de um arquivo de texto e conte quantas vezes a palavra "Python" aparece no arquivo. Exiba o rseultado para o usuário.
# with open("notas.txt", "r", encoding="utf-8") as texto:
#     conteudo= texto.read()
#     contagem=conteudo.count("Python") # Contar a palavra "Python"
#     contagem= conteudo.lower().count("python")
# print(f"A contagem de palavras {contagem} é de... ") 

#  Interação com o sistema operacional
import os # importa o módulo os para interagir com o sistema operacional

# Onde estou?
# print(os.getcwd())

# print(os.listdir())
# print(os.listdir("C:/Users"))

# Criar pastas

# os.mkdir("Ana")
# Criar arquivos
#  
# renomear pastas
# os.rename("Ana","Minha_Pasta")

# Apagar pastas
# os.rmdir("Minha_Pasta")
os.remove("notas.txt") #Excluir arquivos