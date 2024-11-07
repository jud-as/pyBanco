from domain.ContaBancaria import ContaBancaria
class ContaPoupanca(ContaBancaria):
    def __init__(self, aniversario_conta, numero_agencia, tipo_conta, saldo, limite):
        super().__init__(numero_agencia, tipo_conta, saldo, limite)
        self.aniversario_conta = aniversario_conta
        self.taxa_juros = 0.5 # taxa de juros mensal


    def calcular_juros_mensal(self):
        if self.status == "aberta":
            juros = self.saldo * self.taxa_juros
            self.saldo += juros
            self.historico.adicionar_transacao("Juros mensais", juros, self.saldo)
            print(f"Juros mensais no valor de R${juros:.2f} aplicados. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Conta fechada, operação impossível.")
    def __str__(self):
        return (f"\nID Conta: {self.id_conta}"
                f"\nTitular: {self.titular}"
                f"\nAniversario: {self.aniversario_conta}"
                f"\nAgencia: {self.numero_agencia}"
                f"\nTipo: {self.tipo_conta}"
                f"\nSaldo: {self.saldo}"
                f"\nLimite: {self.limite}"
                f"\nStatus: {self.status}")
