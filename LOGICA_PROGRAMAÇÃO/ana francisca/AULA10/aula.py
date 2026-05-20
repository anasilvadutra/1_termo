# Tratamento de erros e depuração
# try e except são usados para lidar com erros de forma controlada, evitando que o programa quebre. O código dentro do bloco try é executando normalmente, mas se ocorrer um erro, o controle é passado para bloco except, onde podemos lidar coma situação de forma apropriada. 

# try:
#     numero = int(input("Digite um núumero: "))
#     resultado = 10 / numero 
#     print("O resultado é:" , resultado)

# except ValueError:
#     print("Erro: Você deve digitar em número válido. ")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero. ")

# except KeyboardInterrupt:
#     print("\n Programa interropido")

# except TypeError: 
#     print("Erro: Tipo de dado inválido.")

# except Exception as erro: 
#     print("Erro inesperado", erro)

# Exercicio 1
# Escreva um programa que solicite ao usuário calcule a méidia de trés números. O programa deve lidar com possiveis erros, como a entrada d valores não numéricos ou a divisão por zero. 

# try: 
#     nu1= float(input("Digite o primeiro numero "))
#     nu2= float(input("Digite o segundo numero "))
#     nu3= float(input("Digite o terciro numero "))

#     média = (nu1+nu2+nu3) / 3
#     print(f"O resultado da médeia é: {média}")

# except ValueError:
#     print("Erro: Você deve digitar em número válido. ")

# except ZeroDivisionError:
#     print("Erro: Não é possivel dividir por zero. ")

# except KeyboardInterrupt:
#     print("\n Programa interropido")

# except TypeError: 
#     print("Erro: Tipo de dado inválido.")

# except Exception as erro: 
#     print("Erro inesperado", erro)

# Explicação de def: A palavra-chave "def" é usada para definir uma função em Python. Uma função é um bloco de código reutiliavel que reliza uma tarefa especifica. 
# return: A palavra-chave "return" é usada para finalizar a execuçao de uma função e retornar um valor para o local onde a função foi chamada. O valor retornado pode ser usado posteriormente no código.

# def nome_da_funcao(parametro1, parametro2):
#     # Corpo da função (código que será executado)
#      resultado = parametro1 + parametro2
#      return resultado

# Exemplo 1:
# def saudacao (nome, idade):
#     nome = input("Digite seu nome:")
#     return f"Olá, {nome} , {idade}!"
# print (saudacao (" ",14))

# Exemplo 2 
# def calcular_media(num1, num2, num3):
#     try:
#         media = (num1+num2+num3) / 3
#         return media
#     except TypeError:
#         return "Erro: Todos os valores devem ser números."
#     except ZeroDivisionError:
#         return "Erro: Não é possivel dividir por zero."
    
# print(calcular_media(10, 20, 30))

# Exemplo 3:
# def valores():
#     print("Digite três valores:")
#     a = int(input("Digite o primeiro valor:  "))
#     b = int(input("Digite o segundo valor:  "))
#     c = int(input("Digite o terceiro valor:  "))
#     return a, b, c
# print(f"O maior valor é: {max(valores())}")

# Exemplo 4 
#  Calcule o dobro de um número fornecido pelo usuario, tratando erros de entrada inválida
# def calcular_dobro():
#     try:
#         valor_digitado = int(input("Digite o valor que deseja :)"))
#         total_dobro = valor_digitado * 2
#         return total_dobro

#     except ValueError:
#         print("Digite um número válido")
# print(f"O calculo é: {calcular_dobro()}")

