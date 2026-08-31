from rich import print
from time import sleep

class Caneta:
    def __init__(self):
        
        # Atributos para utilizar uma caneta
        
        self.caneta_na_mao = False
        self.largar_caneta = False
        self.tampa = True
        self.destampa = False
        self.cor = ["bold black", "bold blue", "bold red", "bold green", "bold purple"]
        self.cor_escolhida = None
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
                self.cor_escolhida = self.cor[0]
                return self.cor[0]
                break
            elif opt == 2:
                print(f'[bold blue] VOCÊ ESCOLHEU A COR AZUL!! [/bold blue]')
                self.cor_escolhida = self.cor[1]
                return self.cor[1]
                break
            elif opt == 3:
                print(f'[bold red] VOCÊ ESCOLHEU A COR VERMELHA!! [/bold red]')
                self.cor_escolhida = self.cor[2]
                return self.cor[2]
                break
            elif opt == 4:
                print(f'[bold green] VOCÊ ESCOLHEU A COR VERDE!! [/bold green]')
                self.cor_escolhida = self.cor[3]
                return self.cor[3]
                break
            elif opt == 5:
                print(f'[bold purple] VOCÊ ESCOLHEU A COR ROXA!! [/bold purple]')
                self.cor_escolhida = self.cor[4]
                return self.cor[4]
                break
            elif opt == 0:
                print(f'Saindo...')
                break
    
    def escrever_texto(self):
        if self.caneta_na_mao: 
            if  self.destampa:
                mensagem = str(input(f'Digite o seu texto: '))
                print(f'[{self.cor_escolhida}]{mensagem}[/{self.cor_escolhida}]')        
            else:
                print(f'[red]TEM QUE DESTAMPAR A CANETA[/red]')
        else:
            print(f'[red]TEM QUE PEGAR A CANETA PRIMEIRO[/red]')

# Objetos da Classe Caneta para teste
escritor = Caneta()
escritor.pegar_caneta()
sleep(1)
escritor.destampar_caneta()
sleep(1)
escritor.escolher_cor_caneta()
sleep(1)
escritor.escrever_texto()