# Exercício 1 
# # 1. contadorde produção (for)
# # Uma esteira processa 10 peças por ciclo. Crie um programa que use um for para contar de 1 a 10 e, para cada número, imprima: "Peça nº X
#  processada com sucesso". No final, exiba "Ciclo de produção concluído"

# for ciclo in range(1,11):
#     print(f"processando lote número {ciclo}...")
#     print("qualidade verificada.[OK]")
#     print("produção do dia finalizada")

# Exercício 2 
# Imagine a produção de frutas em uma feira. Desejo apresentar as frutas banana, manga, melancia,abacaxi. Com uma quantidade de 10 bananas, 5 mangas, 10 melancias e 13 abacaxi.
# No fim da produção  gostaria de ter um total das produções. 

# print("Feira de frutas")
# for ba in range(1,11):
#     print(f"temos {ba} banana")
# print(" esse é a quantidade de banana que temos")

# for man in range(1,6):
#     print(f"temos {man} manga")
# print(" esse é a quantidade de manga que temos")

# for melan in range(1,11):
#     print(f"temos {melan} melancia")
# print(" esse é a quantidade de melancia que temos")

# for abac in range(1,14):
#     print(f"temos {abac} abacaxi")
# print(" esse é a quantidade de abacaxi que temos")
# print ("E é isso que temos na feira de frutas")

# Exercíco 3 
# Montar uma tabuada inicialmente pode ser usado por um valor fixo e depois usar a pergunta  
# print("Tabuada")
# tab = int(input("Digite qual tabuada voce quer"))
# for numero in range(1,11):
#     resultado = tab * numero
#     print(f"{tab} X {numero} = {resultado}")