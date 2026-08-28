from rich import print

class Caneta:
    def __init__(self):
        
        # Atributos para utilizar uma caneta
        
        self.caneta_na_mao = False
        self.largar_caneta = False
        self.tampa = True
        self.destampa = False
        self.cor = ["Preto", "Azul", "Vermelho", "Verde", "Roxo"]
        self.tinta = 100
        self.escrever = False
     
    # Métodos para utilizar uma caneta
    
    def pegar_caneta(self):

        if self.caneta_na_mao == True:
            print("Já estou com uma caneta na mão!!")

        else:
            self.caneta_na_mao = True
            print("Peguei uma caneta!!")
    
    def soltar_caneta(self):
        
        if self.largar_caneta == True:
            print(f'Já soltei a caneta!!')
        else:
            self.largar_caneta = True
            print(f'Deixei a caneta na mesa!!')
            
    def tampar_caneta(self):
        
        if self.tampa == False:
            self.tampa = True
            print(f'Coloquei a tampa da caneta de volta!!')
            
        else:
            print(f'A Caneta já está com a tampa!!')    
    
    def destampar_caneta(self):
        
        if self.destampa == False:
            print (f'Retirei a tampa da caneta!!')
            self.destampa = True
            
        else:
            print(f'A caneta já está destampada!!')
            
    def escolher_cor_caneta(self):
                
        while True:
            print(f'[bold blue] ESCOLHA UMA COR PARA SUA CANETA [/bold blue]')
            print(f'1 - [bold black] PRETO [/bold black]')
            print(f'2 - [bold blue] AZUL [/bold blue]')
            print(f'3 - [bold red] VERMELHO [/bold red]')
            print(f'4 - [bold green] VERDE [/bold green]')
            print(f'5 - [bold purple] ROXO [/bold purple]')
            print(f'0 - [red] CANCELAR ESCOLHAS E SAIR DO PROGRAMA [red]')
            
            print(f'\n[yellow]Sua escolha: [/yellow]')
            opt = int(input(f''))
            
            if opt == 1:
                print(f'[bold black] VOCÊ ESCOLHEU A COR PRETA!! [/bold black]')
                break
            elif opt == 2:
                print(f'[bold blue] VOCÊ ESCOLHEU A COR AZUL!! [/bold blue]')
                break
            elif opt == 3:
                print(f'[bold red] VOCÊ ESCOLHEU A COR VERMELHA!! [/bold red]')
                break
            elif opt == 4:
                print(f'[bold green] VOCÊ ESCOLHEU A COR VERDE!! [/bold green]')
                break
            elif opt == 5:
                print(f'[bold purple] VOCÊ ESCOLHEU A COR ROXA!! [/bold purple]')
                break
            elif opt == 0:
                print(f'Saindo...')
                break
                            
# Objetos da Classe Caneta para teste
escritor = Caneta()
escritor.pegar_caneta()
escritor.pegar_caneta()

escritor.soltar_caneta()
escritor.soltar_caneta()

escritor.tampar_caneta()
escritor.tampar_caneta()

escritor.escolher_cor_caneta()