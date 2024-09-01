from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from insertCidades import *

class cidades:
    def __init__(self, master = None):

        self.container01 = Frame(master)
        self.container01.pack(pady = 20)

        self.container = Frame(master)
        self.container.pack(pady = 5, padx = 20)
        
        self.container02 = Frame(master)
        self.container02.pack(pady = 5, padx = 20)
        
        self.container03 = Frame(master)
        self.container03.pack(pady = 5, padx = 20)

        self.container04 = Frame(master)
        self.container04.pack(pady = 10)


        self.titulo = Label(self.container01, text = "Cadastro de cidades")
        self.titulo.pack()

        self.txtID = Label(self.container, text = "Buscar ID:")
        self.txtID.pack(side = LEFT)
        self.entID = Entry(self.container)
        self.entID["width"] = 5
        self.entID.pack(side = LEFT)
        self.botaoID = Button(self.container, text= "Buscar", width = 5)
        self.botaoID["command"] = self.buscarCidade
        self.botaoID.pack()

        self.txtNome = Label(self.container02, text = "Cidade:")
        self.txtNome.pack(side = LEFT)

        self.entNome = Entry(self.container02)
        self.entNome.pack(side = LEFT)

        self.txtEstado = Label(self.container03, text = "Estado:")
        self.txtEstado.pack(side = LEFT)

        self.entEstado = Entry(self.container03)
        self.entEstado.pack(side = LEFT)
        

        self.botao = Button(self.container04, text = "Cadastrar", width = 12)
        self.botao["command"] = self.cadastrarCidade
        self.botao.pack(side = LEFT)

        self.botaoAlterar = Button(self.container04, text = "Alterar", width = 12)
        self.botaoAlterar["command"] = self.alterarCidade
        self.botaoAlterar.pack(side = LEFT)

        self.botaoExcluir = Button(self.container04, text = "Excluir", width = 12)
        self.botaoExcluir["command"] = self.excluirCidade
        self.botaoExcluir.pack(side = LEFT)

        self.botaoLimpar = Button(self.container04, text = "Limpar", width = 12)
        self.botaoLimpar["command"] = self.limpar
        self.botaoLimpar.pack(side = LEFT)

        self.tree = self.createTreeView(master)

    def limpar(self):
        c = cid()
        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entEstado.delete(0, END)

        messagebox.showinfo("","Campos Limpos")

    def cadastrarCidade(self):
        c = cid()
        
        c.cidade = self.entNome.get()
        c.estado = self.entEstado.get()

        self.entNome.delete(0, END)
        self.entEstado.delete(0, END)

        result = c.cadastrarCidade()
        messagebox.showinfo("Cadastro", result)


        self.atualizarTreeView()

    def alterarCidade(self):
        c = cid()
 
        c.id = self.entID.get()
        c.cidade = self.entNome.get()
        c.estado = self.entEstado.get()

        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entEstado.delete(0, END)

        result = c.updateCidade()
        messagebox.showinfo("Alteração", result)

        self.atualizarTreeView()

    def excluirCidade(self):
        c = cid()

        c.id = self.entID.get()
        
        self.entID.delete(0, END)
        self.entNome.delete(0, END)
        self.entEstado.delete(0, END)

        result = c.deleteCidade()
        messagebox.showinfo("Deletar", result)

        self.atualizarTreeView()

    def buscarCidade(self):
        c = cid()

        c.id = self.entID.get()

        result = c.buscarCidade()
        messagebox.showinfo("Buscar", result)

        self.entID.delete(0, END)
        self.entID.insert(INSERT, c.id)

        self.entNome.delete(0, END)
        self.entNome.insert(INSERT, c.cidade)

        self.entEstado.delete(0, END)
        self.entEstado.insert(INSERT, c.estado)

        
    def createTreeView(self, root):
        c = cid()

        self.tree = ttk.Treeview(root, columns=("ID", "Cidade", "Estado"), show = "headings")
        self.tree.heading("ID", text = "ID")
        self.tree.heading("Cidade", text = "Cidade")
        self.tree.heading("Estado", text = "Estado")
        self.tree.bind("<<TreeviewSelect>>", self.selecionaCidade)
        self.tree.pack(fill = BOTH, expand = True)
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        rows = c.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)
        
        return self.tree
    
    def atualizarTreeView(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        c = cid()
        rows = c.buscarTreeView()

        for row in rows:
            self.tree.insert("", END, values=row)
    
    def selecionaCidade(self, event):
        seleciona_item = self.tree.selection()
        if seleciona_item:
            item = seleciona_item[0]
            values = self.tree.item(item, 'values')

            self.entID.delete(0, END)
            self.entID.insert(INSERT, values[0])

            self.entNome.delete(0, END)
            self.entNome.insert(INSERT, values[1])

            self.entEstado.delete(0, END)
            self.entEstado.insert(INSERT, values[2])


if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    app = cidades(root)
    root.mainloop()