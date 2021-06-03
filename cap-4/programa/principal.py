import tkinter as tk
from tkinter import ttk
import crud as crud

class PrincipalBD:
    def __init__(self, win):
        self.objDB = crud.AppDB()   # Instanciando um objeto do tipo AppDB
        # Componentes Labels
        self.lblCodigo = tk.Label(win, text = 'Código Produto: ')
        self.lblNome = tk.Label(win, text = 'Nome do Produto: ')
        self.lblPreco = tk.Label(win, text = 'Preço')

        # Componentes de entrada
        self.txtCodigo = tk.Entry(bd=3) #bd é o tamanho da borda ao redor do indicador. O padrão: 2px
        self.txtNome = tk.Entry()
        self.txtPreco = tk.Entry()

        # Componentes de Botão ( command tecebe um método da própria classe criado mais adiante)
        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)
        self.btnAtualizar = tk.Button(win, text = 'Atualizar', command= self.fAtualizarProduto)
        self.btnExcluir = tk.Button(win, text="Excluir", command= self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text='Limpar', command=self.fLimparTela)

        #-------------------------------------------------------------------------------------------------
        # Componente TreeView
        #-------------------------------------------------------------------------------------------------
        self.dadosColunas = ("Código", "Nome", "Preço") # poderia ser 0,1 e 2
        self.treeProdutos = ttk.Treeview( win, columns= self.dadosColunas, selectmode='browse')
        # selectmode poderia ser “extended”, “browse” or “none”.

        # Barra de Rolagem
        self.verscrlbar = ttk.Scrollbar(win, orient='vertical', command=self.treeProdutos.yview)
        # h.config (command = t.xview) #para barra de rolagem horizontal
        # v.config (command = t.yview) #para barra de rolagem vertical
        self.treeProdutos.pack(side='right',fill = 'x')
        self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set) # link entre Widget treeView e Scrollbar

        #Use este método para configurar o título da coluna que aparece na parte superior do widget para a coluna especificada por cid, que pode ser um índice de coluna ou um identificador de coluna.
        self.treeProdutos.heading("Código", text='Código')
        self.treeProdutos.heading("Nome", text='Nome')
        self.treeProdutos.heading("Preço", text='Preço')

        self.treeProdutos.column("Código", minwidth = 0, width=100)
        self.treeProdutos.column("Nome", minwidth = 0, width=100)
        self.treeProdutos.column("Preço", minwidth = 0, width=100)

        self.treeProdutos.pack(padx=10,pady=10)
        # Distância especifica o espaço horizontal e vertical em cada lado do objeto
        
        #linca eventos a uma função ou método
        self.treeProdutos.bind("<<TreeviewSelect>>", self.apresentarRegistrosSelecionados)

        #-------------------------------------------------------------------------------------------------
        # Posicionamento dos Componentes na Janela
        #-------------------------------------------------------------------------------------------------
        self.lblCodigo.place(x=100,y=50)
        self.txtCodigo.place(x=250, y= 50)

        self.lblNome.place(x=100,y=100)
        self.txtNome.place(x=250, y=100)

        self.lblPreco.place(x=100,y=150)
        self.txtPreco.place(x=250, y= 150)

        self.btnAtualizar.place(x=100, y=200)
        self.btnCadastrar.place(x =200, y= 200)
        self.btnExcluir.place(x = 300, y=200)
        self.btnLimpar.place(x=400, y=200)

        self.treeProdutos.place(x=100, y=300)
        self.verscrlbar.place(x=605, y=300,height=225)

        self.carregarDadosIniciais() #método criado abaixo

    #-------------------------------------------------------------------------------------------------
    # Carregar Dados Iniciais
    #-------------------------------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
            self.id = 0
            self.iid = 0
            registros = self.objDB.selecionarDados()  #utilizando método do arquivo crud
            print("*********** dados disponíveisno BD **********")
            for item in registros:
                codigo = item[0]
                nome = item[1]
                preco = item[2]
                print("Código: ", codigo)
                print("Nome: ", nome)
                print("Preço: ", preco,"\n")

                self.treeProdutos.insert(parent='',index='end', iid=self.iid, values = (codigo, nome, preco))

                #-parent -  é o ID do item pai ou a string vazia para criar um novo item de nível     superior.
                #-index - é um número inteiro ou o valor final, especificando onde a lista de filhos dos pais para inserir o novo item. Se o índice for menor ou igual a zero, o novo nó é inserido no início e se o índice for maior ou igual ao número atual de filhos, ele é inserido no final. (end é tipo assim, insira no final)
                #- iid - é usado como o identificador do item, iid ainda não deve existir na árvore. Caso contrário, um novo identificador exclusivo é gerado.'''
                self.iid = self.iid + 1
                self.id = self.id + 1
            print("Dados da Base")
        except (Exception) as err:
            print("Ainda não existem dados para carregar,", err)

    #-------------------------------------------------------------------------------------------------
    # Limpar Tela
    #-------------------------------------------------------------------------------------------------
    def fLimparTela(self):
        try:
            print("************** dados disponíveis **************")
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print("Campos Limpos!")
        except:
            print(" Não foi possível limpar os campos!")

    #-------------------------------------------------------------------------------------------------
    # Apresentar Registros Selecionados nos Campos de Inserção
    #-------------------------------------------------------------------------------------------------
    
    def apresentarRegistrosSelecionados(self,event):
        self.fLimparTela()
        for selection in self.treeProdutos.selection(): # usado para deteminar o item afetado pela seleção
            item = self.treeProdutos.item(selection)
            codigo,nome, preco = item["values"][0:3]
            self.txtCodigo.insert(0, codigo) # inserindo automaticamente os valores nos campos de inserção
            self.txtNome.insert(0, nome)
            self.txtPreco.insert(0, preco)
    
    
    #-------------------------------------------------------------------------------------------------
    # LerDados da Tela
    #-------------------------------------------------------------------------------------------------
    def fLerCampos(self):
        try:
            print("************** dados disponíveis **************")
            codigo = int(self.txtCodigo.get()) # pega o valor inserido no campo e transforma e inteiro
            print('codigo', codigo)
            nome = self.txtNome.get()
            print('nome', nome)
            preco = float(self.txtPreco.get())
            print('preço', preco)
            print("Leitura dos Dados com Sucesso!")
        except:
            print("Nao foi possível ler os dados!")
        return codigo, nome, preco
    #-------------------------------------------------------------------------------------------------
    # Cadastrar Produto
    #-------------------------------------------------------------------------------------------------
    def fCadastrarProduto(self):
        try:
            print("*********** dados disponíveis *************")
            codigo, nome, preco = self.fLerCampos() #utiliza funcao criada acima
            self.objDB.inserirDados(codigo, nome, preco) # utiliza funcao do arquivo crud
            self.treeProdutos.insert('', 'end', iid=self.iid, values=(codigo, nome, preco))
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print(" Produto Cadastrado com Sucesso!")
        except:
            print("Não foi possível fazer o cadastro!")
    
    #-------------------------------------------------------------------------------------------------
    # Atualizar Produto
    #-------------------------------------------------------------------------------------------------
    def fAtualizarProduto(self):
        try:
            print("************ dados disponíveis ************")
            codigo, nome, preco = self.fLerCampos() #utiliza função criada acima
            self.objDB.atualizarDados(codigo, nome, preco) #utiliza método do arquivo crud

            #Recarregar dados na Tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais() #utiliza o método criado acima
            self.fLimparTela()
            print("Produto Atualizado com Sucesso!")
        except:
            print("Não foi possível fazer a atualização")

    #-------------------------------------------------------------------------------------------------
    # Excluir Produto
    #-------------------------------------------------------------------------------------------------
    def fExcluirProduto(self):
        try:
            print("************ dados disponíveis ************")
            codigo, nome, preco = self.fLerCampos() #Uuliza função criada acima
            self.objDB.excluirDados(codigo)

            # Recarregar dados na Tela
            self.treeProdutos.delete(*self.treeProdutos.get_children())
            self.carregarDadosIniciais() #utiliza o método criado acima
            self.fLimparTela()   #utiliza função criada acima
            print("Produto Exxcluído com Sucesso!")
        except:
            print("Não foi possível fazer a exclusão do produto")   
    
#-------------------------------------------------------------------------------------------------
# Programa Principal
#-------------------------------------------------------------------------------------------------

janela =  tk.Tk()
principal = PrincipalBD(janela)
janela.title("Bem Vindo a Aplicaçãode Banco de Dados0")
janela.geometry("720x600+10+10")
janela.mainloop()

    

