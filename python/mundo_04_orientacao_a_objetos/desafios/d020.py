from rich import print
from rich.panel import Panel

class Gamer:
    def __init__(self):
        self.nome = ""
        self.nick = ""
        self.jogos_favoritos = []
    
    def registrar_jogador(self):
        self.nome = str(input(f'Informe o nome desse jogador: '))
        self.nick = str(input(f'Informe o nick de {self.nome}: '))
        
        while True:
            
            jogo_favorito = str(input(f'Qual o seu jogo favorito, {self.nick}?: '))
            
            self.jogos_favoritos.append(jogo_favorito)
            self.jogos_favoritos.sort()
            
            resposta = str(input(f'Deseja adicionar mais algum jogo?[S/N]: ')).upper().strip()

            if resposta == "N":
                break
    
    def ficha(self):
        
        ordem_jogos = ""
        
        for i , jogo in enumerate(self.jogos_favoritos, start= 1):
            ordem_jogos += f'{i}° {jogo}\n'
        
        ficha = Panel(
            f'[bold green]Nome do [bright_cyan]jogador[/bright_cyan]: '
            f'[gold1]{self.nome}[/gold1][/bold green]\n'

            f'[bold green]Nick de [bright_cyan]{self.nome}[/bright_cyan]: '
            f'[gold1]{self.nick}[/gold1][/bold green]\n'

            f'[bold green]Jogos favoritos de [bright_cyan]{self.nick}[/bright_cyan]:[/bold green]\n'
            f'[gold1]{ordem_jogos}[/gold1]'
        )
        
        return Panel(ficha, title="Ficha de jogador", width=50 ,style="magenta")
    
# Objetos da claasse

# Player 1
player = Gamer()
player.registrar_jogador()

# Player 2
player2 = Gamer()
player2.registrar_jogador()

# Player 3
player3 = Gamer()
player3.registrar_jogador()

# Player 4
player4 = Gamer()
player4.registrar_jogador()

# Fichas para cada jogador
print(player.ficha())
print(player2.ficha())
print(player3.ficha())
print(player4.ficha())