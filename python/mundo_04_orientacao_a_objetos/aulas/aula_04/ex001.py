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
g1 = Gafanhoto()
g1.nome = "Luis"
g1.idade = 22
g1.aniversario()
print(g1.mensagem())