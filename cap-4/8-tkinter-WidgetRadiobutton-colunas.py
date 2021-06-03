import tkinter as tk 
janela = tk.Tk()

#Agora vamos contruir colunas paralelas - Vamos criar os componenetes
v2 = tk.IntVar()
rotulo = tk.Label(janela, text='Escolha uma linguagem de programação', justify=tk.LEFT, padx=20).grid(row=0, column=1)
opc1 = tk.Radiobutton(janela, text='Python', padx=25, variable=v2, value=1).grid(row=1, column=0, stick=tk.W)
opc2 = tk.Radiobutton(janela, text='C++', padx=25, variable=v2, value=2).grid(row=2, column=0,stick=tk.W)
opc3 = tk.Radiobutton(janela, text='C', padx=25, variable=v2, value=3).grid(row=3, column=0,stick=tk.W)
opc4 = tk.Radiobutton(janela, text='HTML', padx=25, variable=v2, value=4).grid(row=4, column=0,stick=tk.W)
opc5 = tk.Radiobutton(janela, text='CSS3', padx=25, variable=v2, value=5)
opc6 = tk.Radiobutton(janela, text='JS', padx=25, variable=v2, value=6)
opc7 = tk.Radiobutton(janela, text='Java', padx=25, variable=v2, value=7)
opc8 = tk.Radiobutton(janela, text='Ruby', padx=25, variable=v2, value=8)
opc9 = tk.Radiobutton(janela, text='Delph', padx=25, variable=v2, value=9)
opc10 = tk.Radiobutton(janela, text='Arph.Net', padx=25, variable=v2, value=10)
opc11 = tk.Radiobutton(janela, text='MySQL', padx=25, variable=v2, value=11)
opc12 = tk.Radiobutton(janela, text='XML', padx=25, variable=v2, value=12)

## Adiciona Componentes no Grid
 
opc5.grid(row=1, column=1, stick=tk.W)
opc6.grid(row=2, column=1, stick=tk.W)
opc7.grid(row=3, column=1, stick=tk.W)
opc8.grid(row=4, column=1, stick=tk.W)

opc9.grid(row=1, column=2, stick=tk.W)
opc10.grid(row=2, column=2, stick=tk.W)
opc11.grid(row=3, column=2, stick=tk.W)
opc12.grid(row=4, column=2, stick=tk.W)
janela.mainloop()