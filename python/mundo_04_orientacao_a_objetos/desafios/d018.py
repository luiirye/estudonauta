from rich.panel import Panel
from rich import print

class Churrasco:
    def __init__(self):
        self.pessoas = 0
        self.quantidade_carne = 0
        self.preco_carne = 82.40
        self.custo_total = 0
        self.preco_por_pessoa = 0
        
    def churrasco_informacoes(self):
        self.pessoas = int(input(f'Quantas pessoas vão participar?: '))
        self.quantidade_carne = (self.pessoas * 0.4)
        self.custo_total = self.quantidade_carne * self.preco_carne
        self.preco_por_pessoa = self.custo_total / self.pessoas
        
    def mensagem(self):
        mensagem = (
            f'Analisando [green]Churras dos Amigos[/green] com [bold blue]{self.pessoas} convidados[/bold blue]\n'
            f'Cada participante comerá [red]0.4kg de carne[/red] e cada Kg custara [red]R$ {self.preco_carne:.2f}[/red]\n'
            f'O custo total será de [green]R$ {self.custo_total:.2f}[/green]\n'
            f'Cada pessoa pagará [violet]R$ {self.preco_por_pessoa:.2f}[/violet] para poder participar.'
        )
        
        return Panel(mensagem, title="Churrasco com os amigos", width=100, style="white")


# Objetos
churrasco1 = Churrasco()
churrasco1.churrasco_informacoes()

churrasco2 = Churrasco()
churrasco2.churrasco_informacoes()

print(churrasco1.mensagem())
print(churrasco2.mensagem())