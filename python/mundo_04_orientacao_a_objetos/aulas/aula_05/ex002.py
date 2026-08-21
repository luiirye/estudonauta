# Declaração de classe
class Gafanhoto:
    """
    Essa Classe cria um gafanhoto, que é uma pessoa com nome e idade.
    Para criar um novo gafanhoto, use:
    Variável = Gafanhoto(nome, idade)
    """
    
    def __init__(self, nome_gafanhoto = "", idade_gafanhoto = 0): # Método construtor
        # Atributos de instância
        self.nome = nome_gafanhoto
        self.idade = idade_gafanhoto #idade é o atributo da instância por ter o self antes. o valor pós igualdade vem da função.
        
    # Métodos de Instâncias
    def aniversario(self):
        self.idade += 1
            
    def mensagem(self):
        return f'{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade.'

    def __str__(self):
        return "Vou te mostrar uma coisa..."

# Declaração de objetos
g1 = Gafanhoto("Maria", 17) # Instanciação
g1.aniversario() # Método
print(g1.mensagem()) # Método

# print(g1.__doc__)
print(g1)