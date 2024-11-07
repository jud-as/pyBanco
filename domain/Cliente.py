class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.contas = []

    def dados_cliente(self):
        return f'\nNome: {self.nome}\nSobrenome: {self.sobrenome}\nCPF: {self.cpf}'

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def listar_contas(self):
        for conta in self.contas:
            print(conta)