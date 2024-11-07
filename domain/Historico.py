from datetime import datetime
class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.now()
        self.transacoes = []

    def adicionar_transacao(self, tipo, valor, saldo_final):
        transacao = {
            "data": datetime.now(),
            "tipo": tipo,
            "valor": valor,
            "saldo_final": saldo_final
        }
        self.transacoes.append(transacao)
    def imprime(self):
        print("\nHistórico de Transações:")
        print(f"Data da abertura: {self.data_da_abertura.strftime("%d/%m/%Y %H:%M:%S")}")
        for transacao in self.transacoes:
            data = transacao["data"].strftime("%d/%m/%Y %H:%M:%S")
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            saldo_final = transacao["saldo_final"]
            print(f"\n{data}"
                  f"\n{tipo}"
                  f"\nValor: R${valor:.2f}"
                  f"\nSaldo final: R${saldo_final:.2f}")
