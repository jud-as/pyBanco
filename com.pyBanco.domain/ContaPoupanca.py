from ContaBancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self, aniversario_conta, numero_agencia, tipo_conta, saldo, limite):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta



