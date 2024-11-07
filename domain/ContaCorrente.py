from domain.ContaBancaria import ContaBancaria
class ContaCorrente(ContaBancaria):
    def __init__(self, cheque_especial, numero_agencia, tipo_conta, saldo, limite):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        pass

    def __str__(self):
        return (f"\nID Conta: {self.id_conta}"
                f"\nTitular: {self.titular}"
                f"\nCheque especial: {self.cheque_especial}"
                f"\nAgencia: {self.numero_agencia}"
                f"\nTipo Conta: {self.tipo_conta}"
                f"\nSaldo: {self.saldo}"
                f"\nLimite: {self.limite}"
                f"\nStatus: {self.status}")