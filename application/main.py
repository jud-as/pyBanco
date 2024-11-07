from domain.Cliente import *
from domain.ContaBancaria import *
from domain.ContaCorrente import *
from domain.ContaPoupanca import *

def main():

    # Exemplo de uso
    cliente = Cliente("João","Silva" ,12345678900)
    conta1 = ContaCorrente(1, 1001, "Corrente", 0, 1000)
    conta2 = ContaPoupanca("23/03", 1002, "Poupanca", 0, 0)


    # Verificando a associação
    print(f"Contas de {cliente.nome}: {cliente.listar_contas()}")
    print(conta1)
    print(conta2)


if __name__ == "__main__":
    main()
    pass
