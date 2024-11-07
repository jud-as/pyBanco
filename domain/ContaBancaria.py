class ContaBancaria:
    idConta = 0

    def __init__(self, numero_agencia, tipo_conta, saldo, limite):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.idConta += 1

    def consultar_saldo(self):
        pass

    def sacar(self, valor):
        pass

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("\nOperação impossível.")

    def transfere_para(self, destino, valor):
        pass

    def obter_extrato(self):
        pass

    def alterar_titular(self, novo_titular):
        pass

    def fechar_conta(self):
        pass

