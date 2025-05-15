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

def cadastrar_usuario(contas, cpf, nome):
    if cpf in contas:
        print("Usuário já cadastrado.")
        return False
    contas[cpf] = {
        "nome": nome,
        "saldo": 0.0,
        "extrato": "",
        "numero_saques": 0
    }
    print("Usuário cadastrado com sucesso!")
    return True

def depositar(contas, cpf, valor):
    if cpf not in contas:
        print("Usuário não encontrado. Cadastre-se primeiro.")
        return False
    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return False
    contas[cpf]["saldo"] += valor
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    contas[cpf]["extrato"] += f"{data} - Depósito: R$ {valor:.2f}\n"
    print("Depósito realizado com sucesso!")
    return True

def sacar(contas, cpf, valor):
    if cpf not in contas:
        print("Usuário não encontrado. Cadastre-se primeiro.")
        return False
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    saldo = contas[cpf]["saldo"]
    numero_saques = contas[cpf]["numero_saques"]

    if valor <= 0:
        print("Operação falhou! O valor informado é inválido.")
        return False
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
        return False
    if valor > LIMITE_VALOR:
        print("Operação falhou! O valor do saque excede o limite.")
        return False
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return False

    contas[cpf]["saldo"] -= valor
    contas[cpf]["numero_saques"] += 1
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    contas[cpf]["extrato"] += f"{data} - Saque: R$ {valor:.2f}\n"
    print("Saque realizado com sucesso!")
    return True

def exibir_extrato(contas, cpf):
    if cpf not in contas:
        print("Usuário não encontrado. Cadastre-se primeiro.")
        return
    print("\n================ EXTRATO ================")
    extrato = contas[cpf]["extrato"]
    saldo = contas[cpf]["saldo"]
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def listar_usuarios(contas):
    if not contas:
        print("Nenhum usuário cadastrado.")
    else:
        print("\n=== Usuários Cadastrados ===")
        for cpf, dados in contas.items():
            print(f"CPF: {cpf} | Nome: {dados['nome']}")
        print("============================")

def pix_transferencia(contas, remetente_cpf, destinatario_cpf, valor):
    if remetente_cpf not in contas:
        print("Remetente não encontrado. Cadastre o usuário primeiro.")
        return False
    if destinatario_cpf not in contas:
        print("Destinatário não encontrado. Cadastre o usuário primeiro.")
        return False
    if valor <= 0:
        print("Operação falhou! O valor deve ser positivo.")
        return False
    if contas[remetente_cpf]["saldo"] < valor:
        print("Operação falhou! Saldo insuficiente.")
        return False

    contas[remetente_cpf]["saldo"] -= valor
    contas[destinatario_cpf]["saldo"] += valor

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    contas[remetente_cpf]["extrato"] += f"{data} - Pix enviado para {destinatario_cpf}: R$ {valor:.2f}\n"
    contas[destinatario_cpf]["extrato"] += f"{data} - Pix recebido de {remetente_cpf}: R$ {valor:.2f}\n"

    print("Pix realizado com sucesso!")
    return True


while True:
    opcao = input(menu).strip().lower()

    if opcao == "n":
        cpf = input("Informe o CPF (Somente números): ").strip()
        nome = input("Informe o nome completo: ").strip()
        cadastrar_usuario(contas, cpf, nome)

    elif opcao == "d":
        cpf = input("Informe seu CPF: ").strip()
        try:
            valor = float(input("Informe o valor do depósito: "))
        except ValueError:
            print("Valor inválido! Informe um número.")
            continue
        depositar(contas, cpf, valor)

    elif opcao == "s":
        cpf = input("Informe o CPF (Somente números): ").strip()
        try:
            valor = float(input("Informe o valor do saque: "))
        except ValueError:
            print("Valor inválido! Informe um número.")
            continue
        sacar(contas, cpf, valor)

    elif opcao == "e":
        cpf = input("Informe seu CPF: ").strip()
        exibir_extrato(contas, cpf)

    elif opcao == "l":
        listar_usuarios(contas)

    elif opcao == "p":
        remetente_cpf = input("Informe o CPF do remetente: ").strip()
        destinatario_cpf = input("Informe o CPF do destinatário: ").strip()
        try:
            valor = float(input("Informe o valor do Pix: "))
        except ValueError:
            print("Valor inválido! Informe um número.")
            continue
        pix_transferencia(contas, remetente_cpf, destinatario_cpf, valor)

    elif opcao == "q":
        print("Saindo do sistema. Até mais!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
