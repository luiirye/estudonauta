from rich import print
from rich import inspect

class Funcionario:
    
    # Atributos da Classe (Ideia da variável global, mas funciona para TODA A CLASSE)
    empresa = "Curso em vídeo"
    
    def __init__(self, nome = "", cargo = "", setor = ""):
        
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
    
    def apresentacao(self) -> str: # essa seta indica que a função retorna uma string
        
        return f' :handshake: Olá, sou [blue]{self.nome}[/blue] e sou {self.cargo} do setor de {self.setor}, da empresa {Funcionario.empresa}'
        
c1 = Funcionario("Luis", "Programador", "Desenvolvimento" )
c1.empresa = "Estudonauta" # ALTERA SOMENTE LOCALMENTE
print(c1.apresentacao())
inspect(c1)


c2 = Funcionario("Pedro", "Programador", "TI" )
c2.empresa = "Netsystem" # ALTERA SOMENTE LOCALMENTE
print(c2.apresentacao())
inspect(c2)

inspect(Funcionario)