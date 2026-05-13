# CORREÇÃO 
# exercicio 1 
# print("Registro de Veiculo")
# modelo = input("Qual o modelo do seu veículo?...")
# placa = input("Qual a placa do veículo?...")
# print(f"Veículo {modelo} de placa {placa} registrado no sistema. Boa viagem!")

# exercicio 2
# print ("Cáuculo de Autonomia")
# tanque = float(input("Qual é a capacidade de seu tanque e litros "))
# consumo = float(input("Digite o consumo médio por caminhão em Km/l "))
# total = tanque/consumo 
# print(f" Seu caminhão pode percorrer {total} em Km/l")

# exercicio 3 
# print("Conversor de moeda (Frete Internacional)")
# valor_reais = float(input("Qual é o valor em Reais que será convertido?..."))
# taxa_dolar = float(input("Qual é o valor da taxa em dolar em reais?..."))
# total = valor_reais / taxa_dolar
# print(f"O valor convertido é... {total:.2f}")

# exercicio 4 
# print("Média de Entrega")
# tempo1 = int(input("Quanto foi o tempo para concluir na rota 1 em horas?"))
# tempo2 = int(input("Quanto foi o tempo para concluir na rota 2 em horas?"))
# tempo3 = int(input("Quanto foi o tempo para concluir na rota 3 em horas?"))
# media = (tempo1+tempo2+tempo3)
# print(f"A média {media:.2f} de tempo das entregas ")

# exercicio 5 
# print("Monitor de Carga")
# peso = float(input("Qual é o peso atual do seu caminhão?..."))

# if peso < 10:
#     print("Carga Leve")
# elif peso <= 25:
#     print("Carga padrão")
# else: 
#     print("ALERTA: Excesso de peso!")

# exercicio 6
# print("Classificador de destino")
# print("Regiões = N - Norte, S - Sul, qualquer outra - Internacional")
# regiao = input("inserir o código da região: ")
# if regiao == "N".upper() or regiao =="n". lower():
#     print("região norte")
# elif regiao == "S":
#     print("região sul")
# else:
#     print("região internacional")

# exercicio 7
# print("Liberação de saída")
# checklist = input("O checklist foi concluido?[Concluído ou Não Concluído]")
# motorista = input("O motorista foi indentificado? [sim ou não]")
# if checklist == "Concluído" and motorista =="sim":
#     print("Veículo autorizado a iniciar a rota.")
# else: 
#     print("Veículo NÃO autorizado a iniciar a rota. Verificar ckeclist e indentificação do motorista.")

# exercicio 8 
# print("Cálculo de Atrasos")
# total_entregas = int(input("Total de entregas agendadas:..."))
# total_atrasos = int(input("Total de entrgas em Atrasos:..."))
# if total_entregas > total_atrasos * 0.1:
#     print("Necessario otimizar rotas")
# else:
#     print("Logistica Eficicente")

# exercicio 9 
# print("Validação de Calibragem")
# pressao = float(input("Digite a pressão do pneu em PSI:..."))
# if 100 <= pressao <=110:
#     print("Dentro do padrão")
# elif pressao < 100:
#     print("Abaixo derecomendado")
# else:
#     print("Acima de recomendado")

# exercicio 10
# print("Contagem de Embarque")
# import time
# for contagem in range(5,0,-1):
#     time.sleep(1)
#     print(contagem)
#     print("PORTÃO TRANCADO!")

# exercicio 11
# print("Somatorio de frete (Acumulador)")
# while True:
#     valor = float(input("Valor do frete: "))
#     if valor == 0:
#         total += valor
#         print(f"total acumulado {total} do frete")
#         print("FIM!")

# print ("Somatotio de frete (Acumulador) - vesão 2")
# faturamento_total = 0
# valor_frete = -1
# while valor_frete != 0:
#     valor_frete = float(input("valor do frete ou 0 para encerrar"))
#     faturamento_total += valor_frete
#     print(f"Faturamento acumulado:R$ {faturamento_total}")
#     print("calculo executado com sucesso")

#     print ("Somatotio de frete (Acumulador) - vesão 3")
#     b= 0
#     while True:
#         t= int(input("valor Frete..."))
#         c= input("Quer continuar s/n")
#         b += t
#         if c == "s":
#             continue
#         else:
#             break
#         print(f"Faturamento total {b} acumulado")


# exercicio 12 
# print("Monitoramente de Frota")
# maior_km = 0
# for frota in range(1,6):
#     km = float(input(f"Digite a quilometragem do veículo {frota} "))
#     if km > maior_km:
#         maior_km = km
#         print (f"A maior quilometragem registrada é: {maior_km} km ")

# exercicio 13
# print("Sistema de Rastreio")
# codigo_correto = "track99"
# tentativas = 0
# max_tentativas = 3
# while tentativas < max_tentativas:
#     codigo_input = input("código de acesso para o rastreador: :)")
#     if codigo_input == codigo_correto:
#         print("Acesso permitido. iniciando rastreamento...")
#         break
#     else: 
#         tentativas += 1
#         print("acesso negado")
#         if tentativas < max_tentativas:
#             print(f"Tentativas restantes: {max_tentativas-tentativas}")
#         else:
#             print("Rastreamento Bloqueado")