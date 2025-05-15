from datetime import datetime

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo cadastro
[l] Listar usuários
[p] Pix (transferência entre contas)
[q] Sair

=> """

contas = {}

while True:
    opcao = input(menu)

    if opcao == "n":
        cpf = input("Informe o CPF (Somente números): ").strip()

        if cpf in contas:
            print("Usuário já cadastrado.")
            continue

        nome = input("Informe o nome completo: ").strip()

        contas[cpf] = {
            "nome": nome,
            "saldo": 0.0,
            "extrato": "",
            "numero_saques": 0
        }

        print("Usuário cadastrado com sucesso!")

    elif opcao == "d":
        cpf = input("Informe seu CPF: ").strip()

        if cpf not in contas:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            continue

        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Valor inválido! Informe um número.")
            continue

        if valor > 0:
            contas[cpf]["saldo"] += valor
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            contas[cpf]["extrato"] += f"{data} - Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        cpf = input("Informe o CPF (Somente números): ").strip()

        if cpf not in contas:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            continue

        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Valor inválido! Informe um número.")
            continue

        saldo = contas[cpf]["saldo"]
        numero_saques = contas[cpf]["numero_saques"]
        LIMITE_SAQUES = 3
        LIMITE_VALOR = 500

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > LIMITE_VALOR
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["numero_saques"] += 1
            data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            contas[cpf]["extrato"] += f"{data} - Saque: R$ {valor:.2f}\n"
            print("Saque realizado com sucesso!")
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        cpf = input("Informe seu CPF: ").strip()

        if cpf not in contas:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            continue

        print("\n================ EXTRATO ================")
        extrato = contas[cpf]["extrato"]
        saldo = contas[cpf]["saldo"]
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "l":
        if not contas:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n=== Usuários Cadastrados ===")
            for cpf, dados in contas.items():
                print(f"CPF: {cpf} | Nome: {dados['nome']}")
            print("============================")

    elif opcao == "p":
        remetente_cpf = input("Informe o CPF do remetente: ").strip()
        destinatario_cpf = input("Informe o CPF do destinatário: ").strip()

        if remetente_cpf not in contas:
            print("Remetente não encontrado. Cadastre o usuário primeiro.")
            continue
        if destinatario_cpf not in contas:
            print("Destinatário não encontrado. Cadastre o usuário primeiro.")
            continue

        try:
            valor = float(input("Informe o valor do Pix: "))
        except ValueError:
            print("Valor inválido! Informe um número.")
            continue

        if valor <= 0:
            print("Operação falhou! O valor deve ser positivo.")
            continue
        if contas[remetente_cpf]["saldo"] < valor:
            print("Operação falhou! Saldo insuficiente.")
            continue

        contas[remetente_cpf]["saldo"] -= valor
        contas[destinatario_cpf]["saldo"] += valor

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        contas[remetente_cpf]["extrato"] += f"{data} - Pix enviado para {destinatario_cpf}: R$ {valor:.2f}\n"
        contas[destinatario_cpf]["extrato"] += f"{data} - Pix recebido de {remetente_cpf}: R$ {valor:.2f}\n"

        print("Pix realizado com sucesso!")

    elif opcao == "q":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
