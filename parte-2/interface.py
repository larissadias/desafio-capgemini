import tkinter as tk
from tkinter import *
from datetime import datetime

class interface():
    x_pad = 5
    y_pad = 3
    width_entry = 30


    # Cria a janela principal da aplicação
    window = tk.Tk()
    window.title("Sistema de Gerenciamento de Anúncios")


    # Cria as variáveis que serão inseridas pelo usuário
    nome_anuncio = StringVar()
    nome_cliente = StringVar()
    data_inicial = StringVar()
    data_termino = StringVar()
    invest_por_dia = StringVar()


    #Cria os objetos da interface da aplicação
    nome_anuncio_lbl = Label(window, text="Nome do anúncio")
    nome_cliente_lbl = Label(window, text="Cliente")
    data_inicial_lbl = Label(window, text="Data de início")
    data_termino_lbl = Label(window, text="Data de término")
    invest_por_dia_lbl = Label(window, text="Investimento diário")
    nome_anuncio_entry = Entry(window, textvariable=nome_anuncio, width=width_entry)
    nome_cliente_entry = Entry(window, textvariable=nome_cliente, width=width_entry)
    data_inicial_entry = Entry(window, textvariable=data_inicial, width=width_entry)
    data_termino_entry = Entry(window, textvariable=data_termino, width=width_entry)
    invest_por_dia_entry = Entry(window, textvariable=invest_por_dia, width=width_entry)
    anuncios_lista = Listbox(window, width=100)
    anuncios_scroll = Scrollbar(window)
    cadastrar_botao = Button(window, text="Cadastrar anúncio")
    atualizar_botao = Button(window, text="Atualizar cadastro do anúncio selecionado")
    deletar_botao = Button(window, text="Deletar anúncio selecionado")
    ver_todos_botao = Button(window, text="Ver todos os anúncios cadastrados")
    relatorio_botao = Button(window, text="Gerar relatório do anúncio")
    #buscar_botao = Button(window, text="Buscar")

    # Associa os objetos à grid da interface da aplicação
    nome_anuncio_lbl.grid(row=0,column=0, sticky='W')
    nome_cliente_lbl.grid(row=1,column=0, sticky='W')
    data_inicial_lbl.grid(row=2,column=0, sticky='W')
    data_termino_lbl.grid(row=3, column=0, sticky='W')
    invest_por_dia_lbl.grid(row=4, column=0, sticky='W')

    nome_anuncio_entry.grid(row=0, column=1, padx=50, pady=50)
    nome_cliente_entry.grid(row=1, column=1)
    data_inicial_entry.grid(row=2, column=1)
    data_termino_entry.grid(row=3, column=1)
    invest_por_dia_entry.grid(row=4, column=1)

    anuncios_lista.grid(row=0, column=2, rowspan=10)
    anuncios_scroll.grid(row=0, column=6, rowspan=10)
    cadastrar_botao.grid(row=5, column=0, columnspan=2)
    atualizar_botao.grid(row=6, column=0, columnspan=2)
    deletar_botao.grid(row=7, column=0, columnspan=2)
    ver_todos_botao.grid(row=8, column=0, columnspan=2)
    relatorio_botao.grid(row=9, column=0, columnspan=2)
    # buscar_botao.grid(row=10, column=0, columnspan=2)


    # Associa a Scrollbar com a Listbox
    anuncios_lista.configure(yscrollcommand=anuncios_scroll.set)
    anuncios_scroll.configure(command=anuncios_lista.yview)
    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky='WE', padx=x_pad, pady=y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx=0, pady=0, sticky='NS')
        else:
            child.grid_configure(padx=x_pad, pady=y_pad, sticky='N')



    def run(self):
        interface.window.mainloop()