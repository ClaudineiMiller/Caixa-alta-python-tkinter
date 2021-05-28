"""
Cadastro de produtos:

    O Cadastro de Produtos é um software com a finalidade de cadastrar apenas o
produto e seu preço em banco de dados usando o sqlite3.
    Inclui-se também além de visualizar os produtos cadastrados a função de
editar, e excluir cada produto individualmente.
    O programa inteiro foi construido usando a linguagem Python e o Tkinter
"""
from tkinter import ttk as tk
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox as mb


class Caixa_alta():
    """ Classe principal - chama a janela window com todos os widgets. """
    db_name = 'database.db'
    def __init__(self):
        """ Inicializador da janela principal. """
        self.window = ThemedTk(theme='plastik')
        self.window.title("Caixa Alta em Python/Tkinter")
        self.window.resizable(0, 0)
        self.centraliza_window(568, 500)

        self.frame_principal = tk.Frame(self.window)
        self.frame_principal.pack(fill=BOTH)


        self.window.mainloop()

    def centraliza_window(self, comprimento, altura):
        """
        Dimensiona e centraliza a janela.

        recebe duas variáveis:
        comprimento - a largura da janela
        altura - a altura da janela
        """
        # Dimensões da janela
        self.comprimento = comprimento
        self.altura = altura
        # Resolução da tela
        self.comprimento_screen = self.window.winfo_screenwidth()
        self.altura_screen = self.window.winfo_screenheight()
        # Posição da janela
        self.pos_x = (self.comprimento_screen / 2) - (self.comprimento / 2)
        self.pos_y = (self.altura_screen / 2) - (self.altura / 2) - 10

        self.window.geometry(
            "{}x{}+{}+{}".format(
                int(self.comprimento),
                int(self.altura),
                int(self.pos_x),
                int(self.pos_y),
            )
        )

Caixa_alta()
