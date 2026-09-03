from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        
        escolha = ""
        
        match cor.lower().strip():
            case "azul": 
                escolha = "[blue]"
            case "vermelho" | "vermelha":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _:
                escolha = "[white]"
        
        self.cor = escolha
        self.tampada = True
        
    def escrever(self, msg):
        if self.tampada: 
            print(f':prohibited: A {self.cor}caneta[/] está tampada!')
        else:
            print(f'{self.cor}{msg}[/]', end='')
    def quebrar_linha(self, qtd = 1):
        print(f'\n' * qtd, end='')
    
    def tampar(self):
        self.tampada = True
    
    def destampar(self):
        self.tampada = False
    
# Objetos da classe

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá Mundo")
c1.quebrar_linha(4)
c2.escrever("Funciona")
c1.quebrar_linha(3)
c3.escrever("Deu certo")

c1.tampar()
c1.escrever("Será que funciona?")