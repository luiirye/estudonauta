# Declaração de classe
class Gafanhoto:
    def __init__(self): # Método construtor
        # Atributos de instância
        self.nome = ""
        self.idade = 0
        
    # Métodos de Instâncias
    def aniversario(self):
        self.idade += 1
            
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'


# Declaração de objetos
g1 = Gafanhoto() # Instanciação
g1.nome = "Luis" # Atributo
g1.idade = 22 # Atributo
g1.aniversario() # Método
print(g1.mensagem()) # Método

g2 = Gafanhoto()
g2.nome = "Gabryell"
g2.idade = 24
print(g2.mensagem())