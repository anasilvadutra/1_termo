
## 🧠 1. Lógica de Programação Básica com Python

A lógica de programação utiliza estruturas sequenciais, condicionais e de repetição para resolver problemas algorítmicos.

### Variáveis e Tipos de Dados
* `int`: Números inteiros (ex: `idade = 25`).
* `float`: Números decimais (ex: `preco = 49.90`).
* `str`: Textos/Strings (ex: `nome = "Ana"`).
* `bool`: Valores booleanos (`True` ou `False`).

### Estruturas de Controle
```python
# Estrutura Condicional (Se/Senão)
if idade >= 18:
    print("Acesso liberado.")
else:
    print("Acesso bloqueado.")

# Estrutura de Repetição (Loop For)
for i in range(3):
    print(f"Tentativa {i + 1}")
```

---

## 🧹 2. Princípios de Clean Code (Código Limpo)

Escrever código limpo garante que o programa seja legível por humanos e fácil de manter.

### Nomes Significativos
* **Ruim:** `def f(x):` ou `d = 5`
* **Bom:** `def calcular_imposto(faturamento):` ou `dias_para_vencimento = 5`

### Funções Pequenas e de Responsabilidade Única (SRP)
* Cada função deve fazer apenas uma coisa e fazê-la bem.
* Evite funções com dezenas de linhas ou múltiplos objetivos.

### Comentários Necessários vs. Código Autoexplicativo
* Não comente o óbvio. O código deve explicar *o que* faz pelo nome das variáveis.
* Use comentários apenas para explicar o *porquê* de uma decisão complexa.

---

## 📐 3. Formatação Prática no Python (Regras da PEP 8)

O guia de estilo oficial do Python (PEP 8) padroniza a escrita do código.

* **Identação:** Utilize exatamente 4 espaços por nível (não use tabulações).
* **Snake Case:** Nomes de variáveis e funções em minúsculo, separados por underline (`calcular_media_notas`).
* **Espaçamento:** Use linhas em branco para separar funções e blocos lógicos estruturais.

---

## 🎯 4. Proposta de Avaliação Formativa: Projeto Prático

A avaliação formativa acompanha o progresso dos alunos através da construção de um projeto real step-by-step.

### Escopo do Projeto: Sistema de Cadastro e Vendas (CLI)
Os alunos devem desenvolver um programa em linha de comando utilizando Python, aplicando conceitos de lógica e Clean Code.

### Entregas Progressivas
* **Etapa 1 (Estrutura Básica):** Criação do menu de navegação usando loops (`while`) e condicionais (`if/elif/else`).
* **Etapa 2 (Armazenamento):** Utilização de listas e dicionários para salvar dados de produtos e clientes em memória.
* **Etapa 3 (Modularização):** Organização do código dividindo as funcionalidades em funções limpas e específicas.

### Critérios de Avaliação (Rubrica)
* **Funcionalidade:** O programa executa todas as tarefas sem quebras ou erros de runtime?
* **Lógica Aplicada:** Escolha correta de estruturas de repetição, coleções de dados e condicionais.
* **Adoção de Clean Code:** Variáveis bem nomeadas, ausência de código duplicado e funções bem divididas.