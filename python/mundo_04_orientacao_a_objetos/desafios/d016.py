from rich import print

class Funcionario:
    
    def __init__(self):
        
        self.funcionario = ""
        self.setor = ""
        self.cargo = ""
        
    def cadastrar_funcionário(self):
        
        self.funcionario = input(f'Digite o nome desse funcionário: ')
        self.cargo = input(f'Digite o cargo para {self.funcionario}: ')
        self.setor = input(f'Digite o setor para {self.funcionario}: ')
    
    def apresenstar_funcionario(self):
        return print(f'[bold blue]Olá, me chamo[/bold blue] [violet]{self.funcionario}[/violet], sou [violet]{self.cargo}[/violet] [bold blue]do setor de[/bold blue] [violet]{self.setor}[/violet]. [bold blue]Muito Prazer!![/bold blue]') 
        
        
# Objetos da classe
f1 = Funcionario() # instânciando a classse
# Atribuindo valor aos atributos
f1.cadastrar_funcionário()
# Utilizando os atributos
f1.apresenstar_funcionario()

