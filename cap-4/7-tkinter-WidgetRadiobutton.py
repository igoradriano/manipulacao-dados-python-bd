import tkinter as tk 
janela = tk.Tk()
v = tk.IntVar() #define a variavel para status do RadioButton
tk.Label(janela, text='''Escolha uma linguagem de programação''', justify=tk.LEFT, padx=20).pack()
tk.Radiobutton(janela, text='Python', padx=25, variable=v, value=1).pack(anchor=tk.W)
tk.Radiobutton(janela, text='C++', padx=25, variable=v, value=2).pack(anchor=tk.W)
tk.Radiobutton(janela, text='C', padx=25, variable=v, value=3).pack(anchor=tk.W)
tk.Radiobutton(janela, text='HTML', padx=25, variable=v, value=4).pack(anchor=tk.W)
tk.Radiobutton(janela, text='CSS3', padx=25, variable=v, value=5).pack(anchor=tk.W)
tk.Radiobutton(janela, text='JS', padx=25, variable=v, value=6).pack(anchor=tk.W)
tk.Radiobutton(janela, text='Java', padx=25, variable=v, value=7).pack(anchor=tk.W)
tk.Radiobutton(janela, text='Ruby', padx=25, variable=v, value=8).pack(anchor=tk.W)
tk.Radiobutton(janela, text='Delph', padx=25, variable=v, value=9).pack(anchor=tk.W)
tk.Radiobutton(janela, text='Arph.Net', padx=25, variable=v, value=10).pack(anchor=tk.W)
tk.Radiobutton(janela, text='MySQL', padx=25, variable=v, value=11).pack(anchor=tk.W)
tk.Radiobutton(janela, text='XML', padx=25, variable=v, value=12).pack(anchor=tk.W)

janela.mainloop()