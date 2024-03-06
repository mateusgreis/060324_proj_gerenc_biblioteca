from escola import Escola
from aluno import Aluno
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class App:
    def __init__(self, nome: str):
        self.escola = Escola(nome)

        self.janela = Tk()
        self.janela.title(f"Sistema - {self.escola.nome}")

        # Label Matricula
        self.label_matricula = Label(self.janela, text="Matrícula:",
                                     font="Tahoma 14 bold", fg="red")
        self.label_matricula.grid(row=0, column=0)

        # Entry Matricula
        self.txt_matricula = Entry(self.janela, font="Tahoma 14", width=27, state=DISABLED)
        self.txt_matricula.grid(row=0, column=1)

        # Label Nome
        self.label_nome = Label(self.janela, text="Nome:", font="Tahoma 14 bold", fg="red")
        self.label_nome.grid(row=1, column=0)

        # Entry Nome
        self.txt_nome = Entry(self.janela, font="Tahoma 14", width=27)
        self.txt_nome.grid(row=1, column=1)

        # Label Idade
        self.label_idade = Label(self.janela, text="Idade:", font="Tahoma 14 bold", fg="red")
        self.label_idade.grid(row=2, column=0)

        # Entry Idade
        self.txt_idade = Entry(self.janela, font="Tahoma 14", width=27)
        self.txt_idade.grid(row=2, column=1)

        self.cursos = ['Python', 'Javascript', 'Node', 'Django']
        self.label_curso = Label(self.janela, text="Cursos: ", font="Tahoma 14 bold", fg="red")
        self.label_curso.grid(row=3, column=0)

        # Combobox
        self.combo_cursos = ttk.Combobox(self.janela, values=self.cursos, width=25, state='readonly', font='Tahoma 14')
        self.combo_cursos.grid(row=3, column=1)

        # Label Nota
        self.label_nota = Label(self.janela, text="Nota:", font="Tahoma 14 bold", fg="red")
        self.label_nota.grid(row=4, column=0)

        # Entry Nota
        self.txt_nota = Entry(self.janela, font="Tahoma 14", width=27)
        self.txt_nota.grid(row=4, column=1)

        # Buttons
        self.button_adicionar = Button(self.janela, text="Adicionar", font="Tahoma 12 bold", width=7, fg="green", command=self.cadastrarAluno)
        self.button_adicionar.grid(row=5, column=0)

        self.button_editar = Button(self.janela, text="Editar", font="Tahoma 12 bold", width=7, fg="blue", command=self.editarAluno)
        self.button_editar.grid(row=5, column=1)

        self.button_excluir = Button(self.janela, text="Excluir", font="Tahoma 12 bold", width=7, fg="red", command=self.deletarAluno)
        self.button_excluir.grid(row=5, column=2)

        # Frame
        self.frame = Frame(self.janela)
        self.frame.grid(row=6, column=0, columnspan=3) # Columnspan quer dizer quantas colunas de espaço vai ocupar

        self.colunas = ['Matricula', 'Nome', 'Idade', 'Curso','Nota']
        self.tabela = ttk.Treeview(self.frame, columns=self.colunas, show='headings') # headings: mostrar só os cabeçalhos que defini
        for coluna in self.colunas:
            self.tabela.heading(coluna, text=coluna)
            self.tabela.column(coluna, width=110) # Ajustar tamanho da tabela (estética)

        self.tabela.bind("<ButtonRelease-1>", self.selecionarAluno)
        self.tabela.pack()

        self.atualizarTabela()
        self.janela.mainloop()


    def cadastrarAluno(self):
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)

        self.escola.alunos.append(aluno)
        messagebox.showinfo("Sucesso!", "Aluno cadastrado com sucesso!")
        # Depois disso, add comando no button Adicionar
        self.limparCampos()
        self.atualizarTabela()

    # Limpar campos após cadastrar aluno
    def limparCampos(self):
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.delete(0, END)
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.delete(0, END)
        self.txt_idade.delete(0, END)
        self.combo_cursos.set('')
        self.txt_nota.delete(0, END)

    def atualizarTabela(self): # Mostrar dados na tabela após adicionar aluno
        for coluna in self.tabela.get_children():
            self.tabela.delete(coluna) # Primeiro deleto as linhas p/ não gerar duplicada

        for aluno in self.escola.alunos:
            self.tabela.insert("", END, values=(aluno.matricula, aluno.nome, aluno.idade, aluno.curso, aluno.nota))
    # Chamar essa função após função adicionarCadastro

    def selecionarAluno(self, event): # event - Evento que representa uma ação (mover do mouse, algum botão teclado do teclado)
        linha_selecionada = self.tabela.selection()[0] # Pegar o código da linha da tabela (no Tkinter, as tabelas são árvores)
        valores = self.tabela.item(linha_selecionada)['values'] # Função item retorna um dicionário com informações da linha
        self.limparCampos()
        self.txt_matricula.config(state=NORMAL)
        self.txt_matricula.insert(0, valores[0])
        self.txt_matricula.config(state=DISABLED)
        self.txt_nome.insert(0, valores[1])
        self.txt_idade.insert(0, valores[2])
        self.combo_cursos.set(valores[3])
        self.txt_nota.insert(0, valores[4])
        # Adicionar selecionarAluno antes do pack (função bind) p/ mostrar dados nas cx de texto ao clicar na tabela

    def deletarAluno(self):
        matricula = self.txt_matricula.get()
        opcao = messagebox.askyesno("Tem certeza?", "Deseja remover o aluno?")
        if opcao:
            self.escola.removerAluno(matricula)
            messagebox.showinfo("Sucesso!", "Aluno removido com sucesso!")
        self.limparCampos()
        self.atualizarTabela()

    def editarAluno(self):
        matricula = self.txt_matricula.get()
        nome = self.txt_nome.get()
        idade = int(self.txt_idade.get())
        curso = self.combo_cursos.get()
        nota = float(self.txt_nota.get())
        aluno = Aluno(nome, idade, curso, nota)
        aluno.matricula = matricula
        opcao = messagebox.askyesno('Tem certeza?', 'Deseja alterar os dados?')
        if opcao:
            self.escola.editarAluno(aluno)
            messagebox.showinfo('Sucesso!', 'Dados alterados com sucesso!')
        self.limparCampos()
        self.atualizarTabela()




App("Infinity School")