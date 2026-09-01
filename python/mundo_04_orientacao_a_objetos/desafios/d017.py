from rich.panel import Panel
from rich import print

class Produto:
    
    def  __init__(self, nome_produto = "", preco_produto = 0.0):
        self.produto = nome_produto # Atributo para nome do produto
        self.preco = preco_produto # Atributo para preço do produto
    
    def etiqueta_produto(self):
        
        mensagem = (
            f'[bold blue]{self.produto}[/bold blue]: R$ [violet]{self.preco:.2f}[/violet]'
        )

        return Panel(mensagem, title ='Produto' , width=30, style="violet")
    
p1 = Produto("teclado", 120)
print(p1.etiqueta_produto())
p2 = Produto("PC Gamer",10_000)
print(p2.etiqueta_produto())    