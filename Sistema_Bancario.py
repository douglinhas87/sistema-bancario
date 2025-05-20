import json
import os
from datetime import datetime
import getpass

class Usuario:
    def __init__(self, cpf, nome, senha):
        self.cpf = cpf
        self.nome = nome
        self.senha = senha
        self.saldo = 0.0
        self.extrato = ""
        self.numero_saques = 0

    def adicionar_extrato(self, texto):
        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.extrato += f"{data} - {texto}\n"

class Banco:
    LIMITE_SAQUES = 3
    LIMITE_VALOR = 500

    def __init__(self):
        self.usuarios = {}

    def salvar_dados(self, arquivo="usuarios.json"):
        dados = {}
        for cpf, usuario in self.usuarios.items():
            dados[cpf] = {
                "nome": usuario.nome,
                "senha": usuario.senha,
                "saldo": usuario.saldo,
                "extrato": usuario.extrato,
                "numero_saques": usuario.numero_saques
            }
        with open(arquivo, "w") as f:
            json.dump(dados, f, indent=4)
    
    def carregar_dados(self, arquivo="usuarios.json"):
        if not os.path.exists(arquivo):
            return
        with open(arquivo, "r") as f:
            dados = json.load(f)
        for cpf, info in dados.items():
            usuario = Usuario(cpf, info["nome"], info["senha"])
            usuario.saldo = info["saldo"]
            usuario.extrato = info["extrato"]
            usuario.numero_saques = info["numero_saques"]
            self.usuarios[cpf] = usuario

    def cadastrar_usuario(self, cpf, nome, senha):
        if cpf in self.usuarios:
            print("Usuário já cadastrado.")
            return False
        self.usuarios[cpf] = Usuario(cpf, nome, senha)
        print("Usuário cadastrado com sucesso!")
        return True

    def autenticar_usuario(self, cpf, senha):
        usuario = self.usuarios.get(cpf)
        if not usuario:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            return False
        if usuario.senha != senha:
            print("Senha incorreta!")
            return False
        return True

    def depositar(self, cpf, valor):
        if cpf not in self.usuarios:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            return False
        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False
        usuario = self.usuarios[cpf]
        usuario.saldo += valor
        usuario.adicionar_extrato(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
        return True

    def sacar(self, cpf, valor):
        if cpf not in self.usuarios:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            return False

        usuario = self.usuarios[cpf]

        if valor <= 0:
            print("Operação falhou! O valor informado é inválido.")
            return False
        if valor > usuario.saldo:
            print("Operação falhou! Saldo insuficiente.")
            return False
        if valor > self.LIMITE_VALOR:
            print("Operação falhou! O valor do saque excede o limite.")
            return False
        if usuario.numero_saques >= self.LIMITE_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")
            return False

        usuario.saldo -= valor
        usuario.numero_saques += 1
        usuario.adicionar_extrato(f"Saque: R$ {valor:.2f}")
        print("Saque realizado com sucesso!")
        return True

    def exibir_extrato(self, cpf):
        if cpf not in self.usuarios:
            print("Usuário não encontrado. Cadastre-se primeiro.")
            return
        usuario = self.usuarios[cpf]
        print("\n================ EXTRATO ================")
        if not usuario.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(usuario.extrato)
        print(f"\nSaldo: R$ {usuario.saldo:.2f}")
        print("==========================================")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            print("\n=== Usuários Cadastrados ===")
            for cpf, usuario in self.usuarios.items():
                print(f"CPF: {cpf} | Nome: {usuario.nome}")
            print("============================")

    def pix_transferencia(self, remetente_cpf, destinatario_cpf, valor):
        if remetente_cpf not in self.usuarios:
            print("Remetente não encontrado. Cadastre o usuário primeiro.")
            return False
        if destinatario_cpf not in self.usuarios:
            print("Destinatário não encontrado. Cadastre o usuário primeiro.")
            return False
        if valor <= 0:
            print("Operação falhou! O valor deve ser positivo.")
            return False
        remetente = self.usuarios[remetente_cpf]
        destinatario = self.usuarios[destinatario_cpf]

        if remetente.saldo < valor:
            print("Operação falhou! Saldo insuficiente.")
            return False

        remetente.saldo -= valor
        destinatario.saldo += valor

        remetente.adicionar_extrato(f"Pix enviado para {destinatario_cpf}: R$ {valor:.2f}")
        destinatario.adicionar_extrato(f"Pix recebido de {remetente_cpf}: R$ {valor:.2f}")

        print("Pix realizado com sucesso!")
        return True


def main():
    banco = Banco()
    banco.carregar_dados()

    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[n] Novo cadastro
[l] Listar usuários
[p] Pix (transferência entre contas)
[q] Sair

=> """

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "n":
            cpf = input("Informe o CPF (Somente números): ").strip()
            nome = input("Informe o nome completo: ").strip()
            senha = getpass.getpass("Informe uma senha para sua conta: ").strip()
            if banco.cadastrar_usuario(cpf, nome, senha):
                banco.salvar_dados()

        elif opcao == "d":
            cpf = input("Informe seu CPF: ").strip()
            senha = getpass.getpass("Informe sua senha: ").strip()
            if not banco.autenticar_usuario(cpf, senha):
                continue
            try:
                valor = float(input("Informe o valor do depósito: "))
            except ValueError:
                print("Valor inválido! Informe um número.")
                continue
            if banco.depositar(cpf, valor):
                banco.salvar_dados()

        elif opcao == "s":
            cpf = input("Informe o CPF (Somente números): ").strip()
            senha = getpass.getpass("Informe sua senha: ").strip()
            if not banco.autenticar_usuario(cpf, senha):
                continue
            try:
                valor = float(input("Informe o valor do saque: "))
            except ValueError:
                print("Valor inválido! Informe um número.")
                continue
            if banco.sacar(cpf, valor):
                banco.salvar_dados()

        elif opcao == "e":
            cpf = input("Informe seu CPF: ").strip()
            senha = getpass.getpass("Informe sua senha: ").strip()
            if not banco.autenticar_usuario(cpf, senha):
                continue
            banco.exibir_extrato(cpf)

        elif opcao == "l":
            banco.listar_usuarios()

        elif opcao == "p":
            remetente_cpf = input("Informe o CPF do remetente: ").strip()
            senha = getpass.getpass("Informe a senha do remetente: ").strip()
            if not banco.autenticar_usuario(remetente_cpf, senha):
                continue
            destinatario_cpf = input("Informe o CPF do destinatário: ").strip()
            try:
                valor = float(input("Informe o valor do Pix: "))
            except ValueError:
                print("Valor inválido! Informe um número.")
                continue
            if banco.pix_transferencia(remetente_cpf, destinatario_cpf, valor):
                banco.salvar_dados()

        elif opcao == "q":
            print("Saindo do sistema. Até mais!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
