# 💰 Sistema Bancário em Python 3

## 📌 Descrição do Projeto

Este projeto é um sistema bancário simples, desenvolvido com Python 3, que simula operações básicas de um banco via terminal. Ele permite cadastrar usuários, fazer depósitos, saques, transferências via Pix, consultar extratos e listar os usuários.  
Foi criado com fins educacionais para reforçar conceitos como estruturas de dados, controle de fluxo, modularização e manipulação de dados no terminal.

---

## ✅ Funcionalidades Implementadas

- 🧾 **Cadastro de Usuários:** CPF único com nome completo.
- 💵 **Depósito:** Atualiza saldo e extrato com data e hora.
- 🏧 **Saque:** Limite de 3 saques por dia, valor máximo de R$500 por operação.
- 📄 **Extrato:** Exibe todas as movimentações (depósitos, saques, Pix) com data/hora.
- 👥 **Listar Usuários:** Mostra todos os usuários cadastrados com CPF e nome.
- 🔁 **Pix:** Transferência entre contas pelo CPF, com validação e registro no extrato.
- 🚪 **Sair:** Encerra o sistema de forma segura.

---

## 🧰 Tecnologias Utilizadas

- **Python 3** – Linguagem principal
- **datetime** – Registrar data e hora das transações
- **json** – Salvar e carregar os dados
- **os** – Interações com o sistema operacional (ex: limpar tela)
- **getpass** – Entrada de senha oculta no terminal 

---

## 🖥️ Como Usar

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/douglinhas87/sistema-bancario

2. Execute o arquivo Python pelo terminal:
   ```bash
   python3 Sistema_Bancario.py

## 📚 Autor

Desenvolvido por **Douglas Ferraz** 👨‍💻  

