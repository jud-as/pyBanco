from ContaBancaria import ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, cheque_especial, numero_agencia, tipo_conta, saldo, limite):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):

        pass