# Revisão de conteúdo:~
# print = "função de saída de dados para console"
# input = "Função de entrada de dados de usuário via teclado"
# if = "Estrutura de decisão para executar código condicionalmente"
#     elif = "Combinação de else + if para verificar múltiplas condições"
#     else = "Parte opcional de um if que executa código quando a condição do if é falsa"
# for = "Laço de repetição para iterar sobre uma sequência de elementos"
# while = "Laço de repetição para executar código enquanto uma condição fo verdadeira"
# operadores matemáticos: +, - , *, /, //, %, **
# operadores de comparação: ==, !=, >, <, >=, <=
# variavel = "Exemplo de variável para armazenar dados"
# print(variavel)

# Exemplo 1: com print e input 
# nome = input("Digite seu nome: ")
# print(f"Olá, {nome}! Bem-vindo á aula de Python para Desenvolvimento de Sistemas!")

# Exemplo 2: com if, elif e else 
# nota = float(input("Digite a nota do aluno: "))
# if nota >= 7:
#     print ("Aluno aprovado!")
# elif nota >= 5:
#     print("Aluno em recuperação.")
# else: 
#   print("Aluno reprovado.")    

# Exemplo 3: com for
# materiais = ["metal" , "plastico" , "vidro"]
# for material in materiais:
#     print(f"Processando material: {material}.")
#     print(f"Material {material} processado com sucesso! ")
# print(" Fim do processamento de materiais. ")

# EXEMPLOS
# 2. O laço while (Repetições Indeterminadas)
# Use o while quando você não sabe quando vai parar. Ele depende de uma condição (como um sensor de segurança ou um botão de emergência).
# Exemplo: Monitor de Temperatura (Loop infinito Controlado)
# Repete enquanto a temperatura estiver segura 

# import time
# temperatura = 25
# while temperatura < 40:
#     print(f"Temperatura atual {temperatura}°C. Sistema operando...")
#     time. sleep(1)
#     temperatura += 3  #  Simulando o aquecimento da máquina
# print("ALERTA! Temperatura atingiu o limite> Desligando motor...")

#  Lista de temperatura lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]
# for temp in leituras: 
#     while temp > 100:
#         print(f"CRITICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
# print(f"Temperatura está em {temp}°C Operação normal.")
# print("Sistema desligando. Aguardando manutenção.")

# # Produção de peças com controle de material usando continue
# materiais = ["metal", "metal","plastico","metal","vidro","metal"]
# for peca in materiais:
#     if peca != "metal" :
#         print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#         continue #  Pula o restante do código abaixo e vai para a próxima peça
#     # Este código só roda se a peça for de metal
#     print(f"Processando peça de {peca}. Furando e polindo...")
# print("Fim do lote deprodução.")

# EXERCICIOS
# exercicio 1
# Tente criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (simulando uma falha de sensor especifica no item 5)

# numeros = ["1", "2", "3","4", " ouve uma falha no 5", "6","7", "8", "9", "10"]
# for n in numeros:
#     print (f"Veja os numeros {n}")
# print(f" esta pronto")

# exercicio 2 
# Simule um semáforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa para cada cor. Use o continue para pular a cor amarela (simulando um semáforo com defeito que não acende a luz amarela.)

# import time 
# print ("Semáforo")
# cores = (f"verde", "falha no amarelo" , "vermelho")
# for cor in cores:
#     print(f"{cor} ")
#     time.sleep(2)
# print(f"o Semáforo está com uns defeitos")

# #exericicio 3 - Soma de Cargas de Energia (for)
# # Uma fábrica tem 5 máquinas. Peça ao usuário (via input dentro do loop) o consumo em kwh de cada uma das 5 máquinas. Ao final do loop, o programa deve exibir o consumo total da fábrica. 

# print("Soma de carga")
# consumo_total = 0 
# for A in range(1,6):
#     consumo = float(input(f"Digite o consumo da maquina {A} (em KWh: ) "))
#     consumo_total += consumo 

# print (f"\n0 consumo total da fabrica é: {consumo_total: 2f} KWh")

# exercicio 4 - Identificador de peças defeituosas (for + if)
# Percorra uma lista de medidas de peças:
# medidas = [50.1, 49.8, 52.0, 50.0, 48.5]
# o padrão de qualidade aceita apenas peças com extamente 50.0 ou mais.
# Use um for para ler a lista e, para cada peça, diga se ela está "Aprovada" ou "Rejeitada"

# print("Loja de indentificação de peças")
# pecas = [50.1, 49.8, 52.0, 50.0, 48.5]
# for medida in pecas:
#     if medida >= 50.0:
#         print(f"Peças com medida {medida}mm: Aprovada")
#     else:
#         print(f"Peças com medida {medida}mm: Rejeitada")
# print("Fim da avaliação de peças.")

# exercicio 5 - uma balança industrial está pesando um lote de 6 sacos de insumos. O peso ideal de cada saco é 50kg, mas o sistema aceita variações. 
# Crie um programa que peça ao usuário o peso de cada saco (via input dentro do loop) e, para cada um, informe se ele está "Dentro do limite" (entre 48kg e 52kg) ou "Fora do limite". No final, exiba quantos sacos estão dentro do limite.

# print("Balança Industrial")
# sacos_dl = 0
# for saco in range(1,7):
#     peso = float(input(f"Digite o peso de saco {saco} em Kg "))
#     if 48<= peso >= 52:
#         print(f"Saco {saco} com peso {peso}kg: Fora do limite")
#         sacos_dl += 1 #Conta os sacos dentro do limite
#     else: 
#         print(f"Saco {saco} com peso {peso}kg: Fora do limite")
# print(f"Quantidade de sacos dentro do limite: {sacos_dl}")

#  O desafio: Gestão de ciclo térmico
# Você deve criar um programa que monitore a temperatua de uma estufa que processa um lote de 5 peças.
# Regras do sistema: O programa deve rodar em um loop até que 5 peças válidas sejam processadas.
# Para cada peça, peça ao usuário a temperatura atual(input).
# Filtro de erro (continue): Se o usuário digitar uma temperatura negativa, exiba "Erro de leitura no sensor" e use o continue para pedir a temperatura novamente (essa leitura não conta como peça processada).
# Parada de emergencia (break): se a temperatura 