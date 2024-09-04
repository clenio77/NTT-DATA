from datetime import datetime

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.transacoes = []
        self.saques_diarios = 0
        self.limite_saques_diarios = 3
        self.limite_saque = 500.00
        self.ultimo_saque = datetime.now()

    def resetar_saques_diarios(self):
        if datetime.now().date() > self.ultimo_saque.date():
            self.saques_diarios = 0

    def deposito(self, valor):
        if valor <= 0:
            print("O valor do depósito deve ser positivo e maior que zero.")
            return
        self.saldo += valor
        self.transacoes.append({
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'descricao': 'Depósito',
            'valor': valor
        })
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")

    def saque(self, valor):
        self.resetar_saques_diarios()
        if valor <= 0:
            print("O valor do saque deve ser positivo e maior que zero.")
            return
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Limite diário de saques atingido.")
            return
        if valor > self.limite_saque:
            print(f"Limite máximo por saque é de R$ {self.limite_saque:.2f}.")
            return
        if self.saldo < valor:
            print("Saldo insuficiente para realizar o saque.")
            return

        self.saldo -= valor
        self.saques_diarios += 1
        self.ultimo_saque = datetime.now()
        self.transacoes.append({
            'data': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            'descricao': 'Saque',
            'valor': -valor
        })
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def extrato(self):
        if not self.transacoes:
            print("Não foram realizadas movimentações.")
            print("-" * 60)
            print("Extrato da Conta:")
            print("Data                | Descrição           | Valor      | Saldo")
            print("-" * 60)
            return

        print("Extrato da Conta:")
        print("Data                | Descrição           | Valor      | Saldo")
        print("-" * 60)
        saldo_atual = 0.0
        for transacao in self.transacoes:
            saldo_atual += transacao['valor']
            print(f"{transacao['data']} | {transacao['descricao']:<18} | R$ {transacao['valor']:>8.2f} | R$ {saldo_atual:>8.2f}")
        print("-" * 60)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

def menu():
    conta = ContaBancaria()
    while True:
        print("\nMenu:")
        print("1. Depósito")
        print("2. Saque")
        print("3. Extrato")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            valor = float(input("Digite o valor do depósito: "))
            conta.deposito(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor do saque: "))
            conta.saque(valor)
        elif opcao == '3':
            conta.extrato()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
