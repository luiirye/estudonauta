from rich import panel

class Produto:
    
    def  __init__(self, nome_produto = "", preco_produto = 0):
        self.produto = nome_produto # Atributo para nome do produto
        self.preco = preco_produto # Atributo para preço do produto
    
    def etiqueta_produto(self):
        return panel("[purple]{self.produto}[/purple]")
    
    
teste = Produto("Teclado", 120)
print(teste.etiqueta_produto())
        