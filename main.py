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
        self.window.iconphoto(True, PhotoImage(file='image/icon-page.ico'))

        self.centraliza_window(668, 550)

        list_buttons_name = ['Maiúscula', 'Minúscula', 'Título', 'Limpar', 'Copiar']
        buttons_dict = {}
        self.text = StringVar()
        self.ans_to_print = ''

        self.frame_principal = tk.Frame(self.window)
        self.frame_principal.pack(fill=BOTH)

        self.label_top = tk.Label(self.frame_principal,
                                  text='Transform Caracters',
                                  font='Arial 25 bold')
        self.label_top.pack(ipady=30)

        self.frame_buttons = tk.Frame(self.frame_principal)
        self.frame_buttons.pack()

        self.frame_text = tk.Frame(self.frame_principal)
        self.frame_text.pack()

        for name_buttons in list_buttons_name:
            buttons = tk.Button(
                self.frame_buttons,
                text=name_buttons,
                command=lambda name_buttons=name_buttons: self.action(name_buttons))
            buttons.pack(side=LEFT, padx=2, ipadx=8)

        self.entry_text = Text(self.frame_text)
        self.entry_text.pack(side=LEFT, pady=10)
        self.entry_text.focus()

        # scrollbar
        self.scrollbar = tk.Scrollbar(self.frame_text, orient="vertical", command=self.entry_text.yview)
        self.scrollbar.pack(side=LEFT, ipady=165)

        self.window.mainloop()

    def action(self, name):
        if name == 'Maiúscula':
            self.upper()
        elif name == 'Minúscula':
            self.lower()
        elif name == 'Título':
            self.title()
        elif name == 'Limpar':
            self.clear_text_box()
        elif name == 'Copiar':
            self.copy()

    def upper(self):
        text = self.entry_text.get('1.0', END)
        if len(text) <= 1:
            mb.showerror('Atenção!!', 'A caixa está vazia.')
            self.entry_text.focus()
        else:
            self.entry_text.delete('1.0', END)
            self.entry_text.insert('1.0', text.upper())
            self.entry_text.focus()

    def lower(self):
        text = self.entry_text.get('1.0', END)
        if len(text) <= 1:
            mb.showerror('Atenção!!', 'A caixa está vazia.')
            self.entry_text.focus()
        else:
            self.entry_text.delete('1.0', END)
            self.entry_text.insert('1.0', text.lower())
            self.entry_text.focus()

    def title(self):
        text = self.entry_text.get('1.0', END)
        if len(text) <= 1:
            mb.showerror('Atenção!!', 'A caixa está vazia.')
        else:
            self.entry_text.delete('1.0', END)
            self.entry_text.insert('1.0', text.title())
            self.entry_text.focus()

    def clear_text_box(self):
        text = self.entry_text.get('1.0', END)
        self.entry_text.delete('1.0', END)
        self.entry_text.focus()

    def copy(self):
        text = self.entry_text.get('1.0', END)
        if len(text) <= 1:
            mb.showerror('Atenção!!', 'A caixa está vazia.')
        else:
            self.window.clipboard_clear()
            self.window.clipboard_append(text)
            mb.showinfo('Atenção!', 'Conteúdo copiado com sucesso.')
            self.entry_text.focus()

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
