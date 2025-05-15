# Sistema Bancário em Python 3

## Descrição do Projeto

Este projeto é um sistema bancário simples desenvolvido em Python que permite a gestão de contas de usuários, com funcionalidades essenciais como cadastro, depósito, saque, consulta de extrato e transferência via Pix entre contas. O sistema é baseado em linha de comando (terminal) e foi criado para fins educacionais, aplicando conceitos básicos de programação, manipulação de dados e controle de fluxo.

## Funcionalidades Implementadas

- **Cadastro de Usuários:** Permite registrar novos usuários pelo CPF e nome completo, garantindo que o mesmo CPF não seja cadastrado duas vezes.
- **Depósito:** Usuários podem realizar depósitos em suas contas, que são registrados no extrato com data e hora.
- **Saque:** Permite saques com limite diário (3 saques) e limite por operação (R$ 500,00), além de verificar saldo suficiente.
- **Extrato:** Exibe todas as movimentações da conta (depósitos, saques e transferências via Pix), junto com o saldo atual.
- **Listar Usuários:** Exibe a lista de usuários cadastrados com CPF e nome.
- **Pix (Transferência entre contas):** Usuários podem realizar transferências instantâneas entre contas usando o CPF do remetente e do destinatário, com validação de saldo e registro no extrato de ambas as contas.
- **Saída:** Permite sair do sistema de forma segura.

## Tecnologias Utilizadas

- Python 3
- Biblioteca `datetime` para registro das datas e horários das transações.

## Como usar

1. Clone ou faça download do repositório.
2. Execute o arquivo Python pelo terminal:
   ```bash
   python3 Sistema_Bancario.py
