#1.Registro de Veículo: Peça o modelo do veículo e a placa.
# print("oi, iremos ver a placa do seu carro")
# veiculo= input("Digite o modelo do seu veiculo ")
# placa= input("digite sua placa ")
# print(f"seu carro é {veiculo} e a placa á {placa}")
# print("veiculo registrado!")

# 2.Cálculo de Autonomia: Peça a capacidade do tanque de combustível (em litros) e o consumo médio do caminhão (km/l).
# print("iremos descobrir a capacidade do seu automovel")
# tnq=float(input("qual a capacidade do tanque? "))
# cns= float(input("qual é o consumo medio em km/l? "))
# print("A distancia total percorido é:", tnq/cns )
# print(f" Então a capacidade do seu caminhão e de {tnq/cns}")

# 3.Conversor de Moeda (Frete Internacional): O sistema lê o valor de um frete em Dólar (USD).
# print("Convertendo para real ")
# real=(5,00)
# EUA=float(input("Quantos dolares você tem? "))
# print(f"Então você tem {EUA*5,00} reais ")

# 4.Média de Entrega: Peça o tempo de entrega (em horas) de 3 rotas diferentes realizadas por um motorista.
# print("Tempo de entrega")
# T=float(input("quanto tempo demora na 1 rota "))
# H=float(input("quanto tempo demora na 2 rota "))
# D=float(input("quanto tempo demora na 3 rota "))
# media= (T+H+D) / 3
# print(f"A de mora é de {media} ")

# 5.Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# print("Caulculando o peso")
# tonelada = float(input("Digite o peso: ")) 
# if tonelada < 10:
#      print ("Carga Leve!")
# elif tonelada <= 25:
#      print("Carga Padrão.")
# else: 
#    print("Carga em exessão.")   

# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".
# A=print("Da onde você é? "  "Digite N para Região Norte, S para Região Sul e I para Região Intrnacional")
# escolha=input("insira o destino ")
# if escolha== "N":
#     print("Região Norte")
# elif escolha== "S":
#     print("Região Sul")
# else: 
#     print("Região Internacional")

# 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o motorista_identificado == "sim".
# print("liberaçãode saída")
# checklist=input("checklist concluído? ")
# motorista=input("Motorista indentificado? ")
# if checklist== "sim" and motorista=="sim":
#     print("Saida Autorizado!")
# else:
#     print("Saida Não Autorizado!")

# 8.Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# total= int(input("Total de entregas: "))
# atrasos=int(input("Entregas atrasadas: "))
# if atrasos > total * 0.1:
#     print("Necessário Otimizar Rotas")
# else: 
#     print("Logística Eficiente")

# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# print("Caulculando o pressão")
# P = float(input("Digite a pressão: ")) 
# if P <= 99:
#      print ("Pressão está abaixo")
# elif P >= 111:
#       print("Prssão está acima")
# else: 
#       print("Pressão recomendado")

# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5 até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".
# print("Contagem regressiva")
# import time
# for a in range(5,0,-1):
#     time.sleep(1)
#     print(a)
# print("portão trancado!")