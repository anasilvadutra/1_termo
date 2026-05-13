# funções são blocos de código reutilizáveies 
# o "f" python, usado  antes das aspas de uma string (como f "texto {variável}"); indica que se trata de uma f-string (ou formatted string líteral). ele informa ao python que a string contém expressões entre chaves {} que devem ser avaliadas em tempo de execução e substituidas pelos seus valores reais. 

# def saudacao(nome): 
#     return f"olá, {nome}!"

# mensagem = saudacao("maria")
# print(mensagem)

# def age(idade): 
#     return f"olá, {idade}!"
# mensagem = age ("16")
# print(mensagem)

def boas_vindas(nome, cargo):
    print(f"olá, {nome}! você é o novo {cargo}.")

boas_vindas("ana", "desenvolvedora")   
boas_vindas("carlos","gerente")
boas_vindas ("bruno", "professor")

# conversões 
nome=input ("seu nome:")
idade=int(input("sua idade:")) # converte texto para inteiro
print (f"{nome} tem {idade} anos.")