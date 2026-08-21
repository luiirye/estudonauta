from rich import print
from rich.table import Table # table é o módulo e Table é a Classe

tabela = Table(title="Tabela de preços") # Tabela é um objeto, isntanciando a classe Table

tabela.add_column("Nome", justify="right", style = "red")   # Utilizando os métodos da classe Table
tabela.add_column("Preço", justify="center", style="bold blue")  # Utilizando os métodos da classe Table

tabela.add_row("Lápis", "R$1,50")
tabela.add_row("Borracha", "R$5,00")   

print(tabela)