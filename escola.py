# Será o meu "Banco de Dados" e o local onde acessarei os dados
from aluno import Aluno
class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def cadastrarAluno(self, aluno: Aluno): # Já vou pegar a informação do aluno
        self.alunos.append(aluno)

    def editarAluno(self, aluno: Aluno):
        for alu in self.alunos:
            if str(alu.matricula) == str(aluno.matricula): # Se a matrícula for igual (vou clicar e selecionar - tkinter)
                alu.nome = aluno.nome
                alu.idade = aluno.idade
                alu.curso = aluno.curso
                alu.nota = aluno.nota
                return True # Apenas para parar a função quando encontrar a matrícula
        return False # Caso dê algum erro (não encontre a matrícula)

    def removerAluno(self, matricula):
        for aluno in self.alunos:
            if str(aluno.matricula) == matricula: # Converter a matricula p/ string p/ evitar erro com o uuid e função remover aluno da tabela
                self.alunos.remove(aluno)
                return True
        return False

    def listarAlunos(self):
        return self.alunos

if __name__ == "__main__":
    escola = Escola("Infinity School")
    a1 = Aluno("Jonas", 19, "Python", 10)
    a2 = Aluno("Mateus", 30, "FullStack", 9)
    escola.cadastrarAluno(a1)
    escola.cadastrarAluno(a2)
    print(escola.listarAlunos())
    a2.nome = "Mateus Reis"
    print(escola.listarAlunos())
    escola.removerAluno(a1.matricula)
    print(escola.listarAlunos())