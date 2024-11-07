from domain.Cliente import Cliente
from domain.ContaBancaria import ContaBancaria
from domain.ContaPoupanca import ContaPoupanca
from domain.ContaCorrente import ContaCorrente

def main():

    # Exemplo de uso
    cliente = Cliente("João", "Silva", 12345678900)
    cliente_auxiliar = Cliente("Maria", "Tereza", 98765432100)
    conta1 = ContaCorrente(1, 1001, "Corrente", 0, 1000)
    conta2 = ContaPoupanca("23/03", 1002, "Poupanca", 0, 0)
    conta_temporaria = ContaCorrente(1, 1003, "Corrente", 350, 1000)
    conta1.titular = cliente.nome
    conta2.titular = cliente.nome
    conta_temporaria.titular = cliente.nome

    lista_clientes = [cliente, cliente_auxiliar]

    # Associando contas criadas ao cliente
    cliente.contas.append(conta1)
    cliente.contas.append(conta2)
    cliente.contas.append(conta_temporaria)

    # Operações de depósito
    conta1.depositar(100)
    conta2.depositar(400)

    # Operações de saque
    conta1.sacar(50)
    conta2.sacar(50)

    # Operação de transferência
    conta2.transfere_para(conta1, 150)

    # Alteração de titular
    conta1.alterar_titular(cliente_auxiliar.nome)
    cliente_auxiliar.contas.append(conta1)
    cliente.contas.remove(conta1)

    # Operação de fechamento da conta
    conta_temporaria.fechar_conta()

    # Calculando e aplicando juros mensais na conta poupança
    conta2.calcular_juros_mensal()

    # Verificando a associação
    for cliente in lista_clientes:
        print(cliente.listar_contas())

    # Imprimindo histórico de operações de conta
    conta1.obter_extrato()
    conta2.obter_extrato()

if __name__ == "__main__":
    main()
    pass
