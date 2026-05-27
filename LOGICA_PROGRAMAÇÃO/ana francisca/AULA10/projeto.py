# Sistema de Elevador de Prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar.
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir mensagens indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.

print("Olá, bem-vindos ao nosso elevador!")
andt = 0
pss= int(input("Quantas pessoas tem no elevador?  "))
if pss >= 5: 
    print ("ERRO!")
elif pss >= 4:
    print ("Elevador com quantidade adequada.")
else: 
    print("Liberado!")

while True:
    try:
        Dest = int(input("Digite o andar que deseja ir (0-10): "))
        if Dest < 0 or Dest > 10:
           raise ValueError ("Andar não existente. Digite um número de 0 e 10")

        print(f"Elevador se movendo do andar {andt} para o andar {Dest}")
        andt = Dest
        print(f"Chegamos ao andar {andt}")

        if input ("Deseja ir para outro andar? (sim/nao): ").lower()!= 'sim':
            print("Agradeço por ter usado o Elevador! Volte sempre.")
            break
        for listagem in range(10):
            print(f"Andar {listagem} - {'[X]' if listagem == andt else '[ ]'}")

    except ValueError as erro:
        print(f"Erro: {erro}. Tente novamente.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}. Tente novamente.")
        print("Encerrado.")
        break