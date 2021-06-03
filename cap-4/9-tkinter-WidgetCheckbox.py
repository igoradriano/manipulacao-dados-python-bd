import tkinter as tk 
from tkinter import ttk

janela = tk.Tk()

def escolha_carreira():
    v1 = var1.get()
    v2 = var2.get()
    if v1 == 1:
        v1 = 'sim'
        if v2 == 1:
            resp = 'Escolheu Ambas'
            v2 = 'sim'
            
        else:
            resp='Escolheu Gerencial'
            v2 ='não'
    else:
        resp='Escolheu Técnica'
        v2='sim'
        v1='não'
    print(f'Gerencial: {v1}\nTécnica: {v2}\nResposta:{resp} ')

ttk.Label(janela, text='Escolha sua vocação').grid(row=0, column=0, sticky=tk.W)
var1 = tk.IntVar()
ttk.Checkbutton(janela, text='Gerencial', variable=var1).grid(row=1, column=0, sticky=tk.W)
var2 = tk.IntVar()
ttk.Checkbutton(janela, text='Técnica', variable=var2).grid(row=2, column=0, sticky=tk.W)
ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=10)
ttk.Button(janela, text='Mostar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=10)
janela.mainloop()