import tkinter as tk 
from tkinter import messagebox as mb 

def resposta():
    mb.showerror('Resposta', 'Desculpe, nenhuma respota disponível')  #mensagem de erro

def verificador():
    if mb.askyesno('Verificar', 'Realmente quer sair? '):  #mensaem de pergunta yes ou no
        mb.showwarning('SIM', 'Ainda não foi implementado')  #resposta para sim
    else:
        mb.showinfo('NÃO', 'A opção de Sair foi cancelada')  #resposta para nao
    

tk.Button(text='Sair', command=verificador).pack(fill=tk.BOTH) #chama funcao verificador
tk.Button(text='Resposta', command=resposta).pack(fill=tk.BOTH) #chama funcao resposta
tk.mainloop()

#fill opção: determina se deve ocupar mais espaço ou manter as dimensões "próprias".
'''A opção de preenchimento informa ao gerente que o widget deseja preencher todo o espaço atribuído a ele. O valor controla como preencher o espaço; 
BOTH significa que o widget deve se expandir horizontal e verticalmente, 
X significa que ele deve se expandir apenas horizontalmente e 
Y significa que ele deve se expandir apenas verticalmente.'''