from rich import print
from rich import inspect

# print(int.__dict__)

class ContaBancaria:
    """
    Cria uma conta bancária e permite fazer saques e depósitos
    """
    
    def __init__(self, id_conta, nome_titular, saldo_conta = 0):
        # pass
        
        # Atributos
        self.id = id_conta
        self.titular = nome_titular
        self.saldo = saldo_conta
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:.2f}')
        
    
    # Métodos
    def __str__(self):
        return f'A conta {self.id}, pertencente à {self.titular}, possui R$ {self.saldo:.2f} de saldo.'
    
    def depositar(self, valor):
        self.saldo += valor
        print(f'Depósito de R${valor:.2f} autorizado na conta {self.id}')
    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f'Saque de R${valor:.2f} NEGADO. Saldo insuficiente na conta {self.id}')
        else:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} autorizado na conta {self.id}') 

# Objetos
conta_1 = ContaBancaria(112, "Gustavo", 3000)
conta_1.depositar(500)
conta_1.sacar(3000000)
print(conta_1)


inspect(conta_1)