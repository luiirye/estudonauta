from rich import print, emoji
from time import sleep

class Livro:
    
    def __init__(self):
        # Atributos principais da classe
        self.livro = ""
        self.paginas = 1
        self.pagina_atual = 1
        
    def informarLivroPaginas(self):
        self.livro = str(input(f'Qual livro você está lendo?: '))
        self.paginas = int(input(f'Quantas páginas {self.livro} possui?: '))
        
    def exibirLivro(self):
        return print(
            f':book: [bold blue] Você acabou de abrir o livro [violet]"{self.livro}"[/violet] que tem [green]{self.paginas} páginas[/green] no total. Você está na [yellow]página {self.pagina_atual}[/yellow][/bold blue]'
        )
    
    def avancarPaginas(self, quantidade):
        self.avancar = quantidade
         
        if self.pagina_atual + quantidade > self.paginas:
            return print(f':x: [red]Não é possível avançar a quantidade desejada[/red]') 
        else:
            for i in range(self.avancar):
                self.pagina_atual += 1
                print(f'Pág{self.pagina_atual} :arrow_forward: ', end="")
                sleep(1)
            
            print(f'[bold blue]Você avançou {self.avancar} páginas e agora está na [yellow]página  {self.pagina_atual}[/yellow][/bold blue]')
# Objetos
teste = Livro()
teste.informarLivroPaginas()
teste.exibirLivro()
teste.avancarPaginas(10)
teste.avancarPaginas(11)