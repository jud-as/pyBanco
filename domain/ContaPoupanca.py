from domain.ContaBancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self, aniversario_conta, numero_agencia, tipo_conta, saldo, limite):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta


    def calcular_juros_mensal(self):

        pass

    def __str__(self):
        return (f"\nID Conta: {self.id_conta}"
                f"\nTitular: {self.titular}"
                f"\nAniversario: {self.aniversario_conta}"
                f"\nAgencia: {self.numero_agencia}"
                f"\nTipo: {self.tipo_conta}"
                f"\nSaldo: {self.saldo}"
                f"\nLimite: {self.limite}"
                f"\nStatus: {self.status}")
