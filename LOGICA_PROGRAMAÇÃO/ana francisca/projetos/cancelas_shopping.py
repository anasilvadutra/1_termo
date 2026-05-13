# Criar um algoritmo para que:

# Projeto 1:
# Projeto: Precisamos de um algoritmo para gerenciamento de cancelas para um shopping.
# Toda entrada e saída irá ser sinalizada
# Valores para entrada e permanência do veículo deverá ser pergutado
# As entrada deverão ser registradas por placa.
#
# Passo 1:  
# Perguntar informações sobre o veiculo ou forma acesso
# Pressionar o botao para emitir ticket
# Verificar se possui TAG para acesso liberado
# Se possuir erros informar ao usuário

# Passo 2:
# Verificar tempo de permanência
# Valor a ser cobrado

# Passo 3:
# Saída como será?
# Calcular tempo de permanência
# Se for TAG gerar na fatura da TAG
# Pagar ticket
# Devolver ticket na saída

# Passo 4:
# Gerar relatório de entradas e saídas
# Tratamento de Erros
# Revisão do código


print("Bem-Vindo ao Estacionamento!")
forma_acesso= input("O veiculo possui a TAG? (sim/nao):  ")

if forma_acesso == "sim":
    print("TAG indentificada!")
    print("Acesso liberado.")
elif forma_acesso == "nao":
    input("Aperte o botão [ENTER] para imprimir o ticket  ")
    print("Ticket emitido, acesso liberado!")
else:
    print("ERRO: ACESSO NÂO PERMITIDO!")    

tempo= int(input("Quanto tempo você ficara? "))
valor = print ("O valor será" , tempo*12 , "reais")

print(f"Você ficou no shopping por {tempo} horas")
qnt_t =input ("Você realizou o pagamento pelo ticket ou TAG?  ")

if qnt_t == "ticket":
    print(f"Passe o ticket e realize o pagamento de {valor}")
elif qnt_t == "TAG":
    print(f"A fatura da TAG é de {valor}")
else:
    print("ERRO! ")