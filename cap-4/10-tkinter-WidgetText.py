import tkinter as tk 
janela = tk.Tk()
T = tk.Text(janela,height=20, width=30)
T.pack()
T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
tk.mainloop()