import tkinter as tk
from tkinter import messagebox, ttk

def bemvindo():
    # .get() serve para buscar o texto da caixa
    nome_usuario = nome_usuario.get()
    nome_livro = nome_livro.get()
    dias_livro = dias_livro.get()

    if nome_usuario == "" and nome_livro == "" and dias_livro:
        messagebox.showwarning("Aviso", "Por favor digite seu nome :)")
    else:
        messagebox.showinfo("Bem-Vindo", f"Olá {nome_usuario}, logando no sistema!  e sua idade é {nome_livro} e os dias que você quer {dias_livro} ")

# Janela
janela_bemvindo = tk.Tk()
janela_bemvindo.title("biblioteca")
janela_bemvindo.geometry("500x500")

# Componentes
# Labels
lbl_mensagem_usuario = tk.Label(janela_bemvindo, text="Digite seu nome ")
lbl_mensagem_usuario.grid(row=20, column=0, pady=10, padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite o nome do livro ")
lbl_mensagem_idade.grid(row=30, column=0, pady=10, padx=10)

lbl_mensagem_idade = tk.Label(janela_bemvindo, text="Digite o dias que você quer ")
lbl_mensagem_idade.grid(row=40, column=0, pady=10, padx=10)

lbl_mensagem_pais = tk.Label(janela_bemvindo, text="Selecione o tipo do livro")
lbl_mensagem_pais.grid(row=50, column=0, pady=10, padx=10)

# Entrys
usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=20,column=4,pady=10,padx=10)

usuario_nome = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=30,column=5,pady=10,padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=40,column=2,pady=10,padx=10)

usuario_idade = tk.Entry(janela_bemvindo, font=("Arial", 12), width=20)
usuario_nome.grid(row=50,column=2,pady=10,padx=10)
# Componentes de ComboBox
combo_nivel = tk.ttk.Combobox(janela_bemvindo, values=["Livro Geral", "Livro Raro"], width=30)
combo_nivel.grid(row=60, column=2, pady=10, padx=10)


janela_bemvindo.mainloop()
