from rich import print
from rich.panel import Panel

class Churrasco:
    
    #Atributos de classe
    consumo_padrao:float = 0.400 # Cada pessoa come em média 400g de carne
    preco_kg:float = 82.40 # Cada kg de carne custa R$82,40
    
    def __init__(self, titulo, quantidade):
        # Atributos de instância
        self.titulo = titulo
        self.participantes = quantidade
    
    def __str__(self):
        return f'Esse é o {self.titulo} com {self.participantes} pessoas participando.'
    
    def calcular_quantidade_carne(self) -> float: # Retorna um valor Float
        return (self.participantes * Churrasco.consumo_padrao)
    
    def calcular_custo_total(self) -> float: # Retorna um valor Float
        return (self.calcular_quantidade_carne() * Churrasco.preco_kg)
        
    def calcular_custo_individual(self) -> float: # Retorna um valor Float
        return (self.calcular_custo_total() / self.participantes)
    
    def analisar(self):
        
        conteudo = f"Analisando [bold green]{self.titulo}[/bold green] com [bold purple]{self.participantes} participantes.[/bold purple]"
        conteudo += f"\n[bold blue]Cada participante comerá [yellow]{Churrasco.consumo_padrao}kg e cada Kg custa R${Churrasco.preco_kg:,.2f}[/yellow][/bold blue]"
        conteudo += f"\nRecomendo comprar [pink]{self.calcular_quantidade_carne():.3f}Kg de carne.[/pink]"
        conteudo += f"\nO custo total será de [bold green]R$ {self.calcular_custo_total():,.2f}[/bold green] no total."
        conteudo += f"\nCada pessoa irá pagar [purple]R$ {self.calcular_custo_individual():,.2f} para participar.[/purple]"
        painel = Panel(conteudo, title=self.titulo, width=80)
        print(painel)
        
c1 = Churrasco("Churras dos Amigos", 15)
print(c1)
c1.analisar()

c2 = Churrasco("Festa do fim de ano", 80)
print(c2)
c2.analisar()
# Consumo padrão: 400g por pessoa
# Preço: R$82,40/kg