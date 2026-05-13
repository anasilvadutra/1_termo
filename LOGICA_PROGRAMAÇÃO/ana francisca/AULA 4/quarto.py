# #1. o laço 'for' (repetições determinadas)
# #use o 'for' quando você sabe exatamente quantas vezes algo deve acontecer (como ler 10 sensores ou processar uma lista de peças). 
# #exemplo: relatório de produção diária 
# #imagine que você tem uma meta de produzir 5 lotes e quer numerar cada um: 

# exemplo1
# for lote in range (1, 6):
#     print(f"processando lote número {lote}...")
#     print("qualidade verificada.[OK]")
#     print("produção do dia finalizada")

# #exemplo2 
# for b in range(10):
#     print(f"quantidade total {b} foi...")

# # exemplo3 
# # imagine o seguinte cenário, iremos produzir 20 discos de vinil.
# for vinil in range(1,21):
#     print (f"produção de {vinil},diária")

# #exemplo4 
# pecas = ["engrenagem","eixo","rolamento","parafuso","martelo", "prego","chave de fende", "alicate"]
# itempecas = ["cilindica","duplo","conica","prego","orelha","redondo","phillips","universal"]


# for item in pecas:
#     print(f"item em estoque:{item} e {itempecas}")

# exemplo5 
# imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opnião você deseja e a partir da seleção ele listar os produtos

print("Menu de opções de filme e séries")
print("1 para filmes 2 para séries")


