from tkinter import ttk as tk
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox as mb


class Teste():
    """ Classe principal - chama a janela window com todos os widgets. """
    db_name = 'database.db'
    def __init__(self):
        """ Inicializador da janela principal. """
        self.window = ThemedTk(theme='plastik')
        self.window.title("Caixa Alta em Python/Tkinter")
        self.window.resizable(0, 0)
        self.window.geometry('500x400')

        users = {"Test":"127.0.0.0", "Test2":"128.0.0.0"}
        row = 1
        for name in users:
            user_button = tk.Button(self.window, text=name, command=lambda name=name: self.a(name))
            user_button.grid(row = row, column = 0)
            row+=1

        self.window.mainloop()


    def a(self, name):
        print(name)

Teste()
