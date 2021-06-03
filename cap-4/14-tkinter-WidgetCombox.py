import tkinter as tk
from tkinter import ttk


# Criação de uma janela tkinter
janela = tk.Tk()
janela.title("Combox")
janela.geometry('500x200')


# Componente Label
ttk.Label(janela, text='Combox Widget', background='green', foreground='white',
          font=('Times New Roman',15)).grid(row=0,column=1)
# Componente Label
ttk.Label(janela, text='Selecione um mês: ', font=('Times New Roman', 15)).grid(column=0,row=5, padx=10,pady=25)

#Componente Combox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width=27, textvariable=n)

#Adiçãode intensno Combox
escolha['values'] = ('Janeiro',
                     'Fevereiro',
                     'Maço',
                     'Abril',
                     'Maio',
                     'Junho',
                     'Julho',
                     'Agosto',
                     'Stembro',
                     'Outubro',
                     'Novembro',
                     'Dezembro')
escolha.grid(column=1,row=5)
escolha.current()  #posso colocar um indice, por exemplo, 1 vai aparecer janeiro como padrão, 10 vai aparecer outubro
janela.mainloop()
