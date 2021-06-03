import tkinter as tk 


def mostrar_nomes():#É implementada a função “mostrar_nomes”, que vai exibir na linha de comando os nomes que estão escritos nas instâncias “e1” e “e2” do componente “entry”.
    print(f"Nome: {e1.get()}\nSobrenome: {e2.get()}")


janela = tk.Tk()
janela.title("Aplicação GUI com o widget Entry")
tk.Label(janela, text='Nome').grid(row=0, column=0)  #criacao das Labels
tk.Label(janela, text='Sobrenome').grid(row=1, column=0) 
e1 = tk.Entry(janela) #São feitas as instâncias “e1” e “e2” do componente entry.
e2 = tk.Entry(janela)

'''w = Entry( master, option, ... )
Parâmetros
master - representa a janela principal.
options - Aqui está a lista das opções mais comumente usadas para este widget. Essas opções podem ser usadas como pares de valores-chave separados por vírgulas.
ex:bg,bd,comando,cursor,fonte,selecao de exportacoes,fg...
'''

e1.grid(row=0, column=1) #“e1” e “e2” são posicionados na janela.
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair', command=janela.quit).grid(row=3, column=0, pady=10)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3, column=1, sticky='', pady=10)
#São instanciados objetos do componente “botão”. Em especial, na linha 17, a função “mostrar_nomes” é associada ao comportamento do botão.
tk.mainloop()
#ticky - o que fazer se a célula for maior do que o widget. Por padrão, com sticky = '', o widget é centralizado em sua célula. pegajoso pode ser a concatenação de sequência de zero ou mais de N, E, S, W, NE, NW, SE e SW, direções da bússola indicando os lados e cantos da célula aos quais o widget se fixa.

#padx, pady - Quantos pixels preencher o widget, horizontal e verticalmente, fora das bordas de v.