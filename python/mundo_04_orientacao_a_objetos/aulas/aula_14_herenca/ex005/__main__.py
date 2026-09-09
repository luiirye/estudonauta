from rich import print, inspect
from classesex005 import Aluno, Professor, Funcionario
    
a1 = Aluno("Luis Felipe", 22, "Engenharia de Computação", "T01")
print(a1.__dict__)
a1.fazer_matricula()
#inspect(a1, methods=True)

p1 = Professor("Samuel", 37, "Biologia", "Mestre")
p1.fazer_aniversario()
p1.dar_aula()
#inspect(p1, methods=True)

f1 = Funcionario("Webster", 27, "Programador", "Núcleo de inovação e tecnologia jurídica")
f1.bater_ponto()
#nspect(f1, methods=True)