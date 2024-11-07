 Cl# pyBanco
### Sistema Bancário feito em Python.
### Disciplina: Novas Tecnologias
### Orientador: Adam Smith  
## Descrição do projeto:


### 1. Classe ContaBancaria:
### Atributos:
```
I.   numero_agencia : número da agência onde a conta está registrada.
II.  tipo_conta : tipo de conta bancária (corrente, poupança, etc.).
III. saldo : saldo da conta
IV.  limite : limite para pagamentos
```
### Métodos:
```
I.   consultar_saldo(self) : retorna o saldo atual da conta.
II.  saca(self, valor) : retira um valor do saldo
III. deposita(self, valor): adiciona valor no saldo
IV.  transfere_para(self, destino, valor) : transfere um valor do cliente para outro cliente destino
V.   obter_extrato(self) : retorna um extrato detalhado das transações realizadas na conta.
VI.  alterar_titular(self, novo_titular) : altera o nome do titular da conta.
VII. fechar_conta(self) : fecha a conta bancária, transferindo o saldo restante para o titular.
```
-------------------------------------------------------------------------
### 2. Classe Historico:
### Atributos:
```
I.   data_da _abertura: guardar a data da abertura da conta
II.  transacoes : guarda as transações realizadas pelo cliente
```
### Métodos:
```
I.   imprime(self) : imprime as transações realizadas por cada cliente
```
-------------------------------------------------------------------------
### 3. Classe Cliente:
### Atributos:
```
I.   nome : nome do cliente
II.  sobrenome : sobrenome do cliente
III. cpf : cpf do cliente
```
### Métodos:
```
I.   dados_cliente(self): retorna os dados do cliente
```
-------------------------------------------------------------------------
### Classe ContaPoupanca (herda de ContaBancaria):
### Atributos:
```
I.   aniversario_conta : data de aniversário da conta poupança, quando os juros são aplicados.
```
### Métodos:
```
I.   calcular_juros_mensal(self) : calcula e aplica juros mensais ao saldo da conta poupança.
```
-------------------------------------------------------------------------
### Classe ContaCorrente (herda de ContaBancaria):
### Atributos:
```
I.   cheque_especial : indica se a conta corrente possui cheque especial ou não.
```
### Métodos:
```
I.   utilizar_cheque_especial(self, valor) : permite que o titular utilize o cheque especial para cobrir um saldo insuficiente.
```
-------------------------------------------------------------------------


