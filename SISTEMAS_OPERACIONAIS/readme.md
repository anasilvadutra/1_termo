## 💻 1. Conceitos de Sistemas Operacionais (S.O.)

O Sistema Operacional é a camada de software que gerencia o hardware e fornece a base para os aplicativos.

### Funções Principais
* **Gerenciamento de Processos:** Criação, agendamento e finalização de programas.
* **Gerenciamento de Memória:** Alocação de RAM para cada tarefa ativa.
* **Gerenciamento de Arquivos:** Organização e controle de acesso a dados em disco.

---

## 🧭 2. Indicação de Sistemas Operacionais e Distribuições

### Microsoft Windows
* Focado em uso corporativo, ambiente de escritório e jogos.
* Código fechado e interface gráfica altamente padronizada.

### Distribuições Linux (Ecossistema Aberto)
* **Ubuntu / Debian:** Ideais para iniciantes e servidores robustos.
* **Fedora / Red Hat (RHEL):** Focados em inovação corporativa e estabilidade.
* **Alpine Linux:** Ultra-leve, amplamente usado em contêineres Docker.

---

## ⌨️ 3. Operação de S.O. via CLI (Interface de Linha de Comando)

A CLI (Command Line Interface) permite controlar o S.O. diretamente por texto, consumindo menos memória que a interface gráfica.

### Comandos Essenciais de Navegação (Comparativo)


| Operação | Windows (CMD / PowerShell) | Linux (Bash) |
| :--- | :--- | :--- |
| Listar diretório | `dir` | `ls` |
| Mudar de pasta | `cd` | `cd` |
| Limpar tela | `cls` | `clear` |

---

## 🪟 4. Operação do Windows via CLI (CMD e PowerShell)

O Windows possui dois ambientes de terminal nativos principais:
* **CMD (Prompt de Comando):** Legado, focado em compatibilidade com scripts antigos.
* **PowerShell:** Moderno, baseado em objetos e na plataforma .NET, voltado para automação pesada.

### Comandos de Diagnóstico no Windows:
* `ipconfig` -> Exibe configurações de rede e endereços IP.
* `ping [host]` -> Testa a conectividade com um servidor na rede.
* `tasklist` -> Lista todos os processos em execução na máquina.

---

## 📂 5. Manipulação de Pastas, Usuários e Variáveis no Windows

### Gerenciamento de Arquivos e Pastas
* Criar pasta: `mkdir C:\AulasSO`
* Excluir pasta: `rmdir /s C:\AulasSO`

### Gerenciamento de Usuários (Requer Privilégios de Administrador)
* Criar novo usuário: `net user AlunoSO SenhaForte123 /add`
* Adicionar a um grupo: `net localgroup Administradores AlunoSO /add`

### Lidando com Variáveis de Ambiente
Variáveis guardam dados voláteis e caminhos globais do sistema.
* Exibir uma variável: `echo %USERNAME%` ou `echo %PATH%`
* Criar variável temporária: `set MINHA_VARIAVEL=Aula01`

---

## 🛡️ 6. Segurança Cibernética no Nível do S.O.

A segurança do sistema operacional mitiga riscos de invasões e vazamento de dados.

### Pilares de Proteção
* **Princípio do Menor Privilégio:** Usuários comuns não devem rodar tarefas como Administrador/Root por padrão.
* **Gerenciamento de Patches:** Atualização constante do núcleo (kernel) contra vulnerabilidades exploradas (Exploits).
* **Controle de Portas e Firewall:** Fechamento de portas lógicas não utilizadas para evitar varreduras de rede externas.