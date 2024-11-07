from domain.Historico import Historico


class ContaBancaria:
    _next_id_conta = 1

    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.titular = ""
        self.id_conta = ContaBancaria._next_id_conta
        ContaBancaria._next_id_conta += 1
        self.status = "aberta"
        self.historico = Historico()

        # Registro de abertura de conta no histórico
        self.historico.adicionar_transacao("Abertura de conta", saldo, saldo)

    def consultar_saldo(self):
        return self.saldo

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente.')

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("\nOperação impossível.")

    def transfere_para(self, destino, valor):

        # Verifica possibilidade de transferencia
        if not isinstance(destino, ContaBancaria):
            print("Conta de destino não válida.")
            return False
        else:
            if valor > self.saldo:
                print("Saldo insuficiente.")
                return False

        # Realiza transferência
        self.saldo -= valor
        destino.depositar(valor)

    def obter_extrato(self):
        pass

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular

    def fechar_conta(self):
        if self.status == "fechada":
            print("\nConta já fechada.")
            return

        saldo_final = self.saldo
        self.sacar(saldo_final)
        self.status = "fechada"
        print(f"\nConta {self.id_conta} fechada. Valor de R${saldo_final:.2f} transferido para o titular {self.titular}.")
