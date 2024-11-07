from datetime import datetime

# Classe Cliente
class Cliente:
    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def dados_cliente(self):
        return f"{self.nome} {self.sobrenome}, CPF: {self.cpf}"

# Classe Historico
class Historico:
    def __init__(self):
        self.data_da_abertura = datetime.now()
        self.transacoes = []

    def imprime(self):
        print("Data de abertura:", self.data_da_abertura.strftime("%d/%m/%Y %H:%M:%S"))
        for transacao in self.transacoes:
            print(transacao)

# Classe ContaBancaria
class ContaBancaria:
    def __init__(self, numero_agencia, tipo_conta, saldo, limite, titular):
        self.numero_agencia = numero_agencia
        self.tipo_conta = tipo_conta
        self.saldo = saldo
        self.limite = limite
        self.titular = titular
        self.historico = Historico()

    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"

    def saca(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.transacoes.append(f"Saque de R${valor:.2f}")
        else:
            print("Saldo insuficiente para saque.")

    def deposita(self, valor):
        self.saldo += valor
        self.historico.transacoes.append(f"Depósito de R${valor:.2f}")

    def transfere_para(self, destino, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.transacoes.append(f"Transferência de R${valor:.2f} para conta {destino.numero_agencia}")
        else:
            print("Saldo insuficiente para transferência.")

    def obter_extrato(self):
        self.historico.imprime()

    def alterar_titular(self, novo_titular):
        self.titular = novo_titular
        self.historico.transacoes.append(f"Titular alterado para {novo_titular.dados_cliente()}")

    def fechar_conta(self):
        saldo_final = self.saldo
        self.saldo = 0
        self.historico.transacoes.append("Conta encerrada.")
        return f"Conta encerrada com saldo final de R${saldo_final:.2f}"

# Classe ContaPoupanca
class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, titular, aniversario_conta):
        super().__init__(numero_agencia, "Poupança", saldo, limite, titular)
        self.aniversario_conta = aniversario_conta

    def calcular_juros_mensal(self, taxa_juros):
        juros = self.saldo * taxa_juros
        self.saldo += juros
        self.historico.transacoes.append(f"Juros aplicados de R${juros:.2f}")

# Classe ContaCorrente
class ContaCorrente(ContaBancaria):
    def __init__(self, numero_agencia, saldo, limite, titular, cheque_especial=False):
        super().__init__(numero_agencia, "Corrente", saldo, limite, titular)
        self.cheque_especial = cheque_especial

    def utilizar_cheque_especial(self, valor):
        if self.cheque_especial and valor <= (self.saldo + self.limite):
            self.saldo -= valor
            self.historico.transacoes.append(f"Uso do cheque especial de R${valor:.2f}")
        else:
            print("Cheque especial não disponível ou limite insuficiente.")

# Exemplo de uso
cliente = Cliente("João", "Silva", "123.456.789-00")
conta_corrente = ContaCorrente("001", 1000, 500, cliente, True)
conta_corrente.consultar_saldo()
conta_corrente.deposita(200)
conta_corrente.saca(300)
conta_corrente.utilizar_cheque_especial(500)
conta_corrente.obter_extrato()
