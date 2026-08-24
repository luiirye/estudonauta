from rich import print

class Produto:
    
    def  __init__(self, nome_produto, preco_produto):
        self.produto = nome_produto # Atributo para nome do produto
        self.preco = preco_produto # Atributo para preço do produto
    
    def Etiqueta(self):
        