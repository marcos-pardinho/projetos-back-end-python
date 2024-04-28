class ContaBancaria:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo
        self.transacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.transacoes.append(f"Depósito de {valor}")
        print(f"Depósito de {valor} realizado. Novo saldo: {self.saldo}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.transacoes.append(f"Saque de {valor}")
            print(f"Saque de {valor} realizado. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente.")

    def transferir(self, destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.transacoes.append(f"Transferência de {valor} para {destino.nome}")
            print(f"Transferência de {valor} para {destino.nome} realizada com sucesso.")
        else:
            print("Saldo insuficiente para transferência.")

    def verificar_saldo(self):
        print(f"Saldo atual: {self.saldo}")

    def imprimir_transacoes(self):
        print("Histórico de transações:")
        for transacao in self.transacoes:
            print(transacao)


def main():
    print("Bem-vindo ao sistema bancário!")

    nome1 = input("Digite o nome do primeiro titular da conta: ")
    conta1 = ContaBancaria(nome1)

    nome2 = input("Digite o nome do segundo titular da conta: ")
    conta2 = ContaBancaria(nome2)

    while True:
        print("\nEscolha uma opção:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Verificar saldo")
        print("5. Histórico de transações")
        print("6. Sair")

        opcao = input("Digite o número da opção desejada: ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: "))
            conta1.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: "))
            conta1.sacar(valor)
        elif opcao == "3":
            valor = float(input("Digite o valor a ser transferido: "))
            conta1.transferir(conta2, valor)
        elif opcao == "4":
            print("Saldo do primeiro titular:")
            conta1.verificar_saldo()
            print("Saldo do segundo titular:")
            conta2.verificar_saldo()
        elif opcao == "5":
            print("Transações do primeiro titular:")
            conta1.imprimir_transacoes()
            print("Transações do segundo titular:")
            conta2.imprimir_transacoes()
        elif opcao == "6":
            print("Obrigado por usar nosso sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


if __name__ == "__main__":
    main()
