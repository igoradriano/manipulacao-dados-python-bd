import tkinter as tk
from tkinter import ttk

def monstrar_valores():
    print(w1.get(),'-',w2.get())

janela = tk.Tk()
w1 = ttk.Scale(janela, from_=0, to=50)
w1.pack()

w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
w2.pack()

ttk.Button(janela, text='Monstrar a Escala', command=monstrar_valores).pack()
janela.mainloop()