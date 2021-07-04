# -*- coding: utf-8 -*-
#
# Desafio de Programação Capgemini (2021) 
# 2ª Parte - Sistema de Cadastro de Anúncios.
#
# O código recebe os dados do anúncio e gera um relatório 
# contendo: o valor total investido, a quantidade máxima de visualizações,
# a quantidade máxima de cliques e a quantidade máxima de compartilhamentos.
#
# Autora: Ana Larissa Dias - larissa.engcomp@gmail.com
# Julho 2021

from interface import *
import bancodedados as core
import tkinter.font as tkFont
from datetime import datetime

app = None

def cadastrar():
    core.insert(app.nome_anuncio.get(), app.nome_cliente.get(), app.data_inicial.get(), app.data_termino.get(), app.invest_por_dia.get())
    visualizar()

def atualizar():
    core.update(selected[0],app.nome_anuncio.get(),app.nome_cliente.get(),app.data_inicial.get(), app.data_termino.get(), app.invest_por_dia.get())
    visualizar()

def visualizar():
    rows = core.view()
    app.anuncios_lista.delete(0, END)
    for r in rows:
        app.anuncios_lista.insert(END, r)

def gerar_relatorio():
    newWindow = Toplevel(app.window)
    titulo_relatorio = "Relatório do Anúncio " + app.nome_anuncio.get()
    newWindow.title(titulo_relatorio)
    newWindow.geometry("600x200")
    labelFont1 = tkFont.Font(family="calibre", size=12) #, weight="bold")
    Label(newWindow, text=relatorio(), font=labelFont1, justify=LEFT, anchor="w").pack()
    botao_sair = Button(newWindow, text='OK', command=newWindow.destroy)
    botao_sair.pack()

def deletar():
    id = selected[0]
    core.delete(id)
    visualizar()

def relatorio():
    d2 = datetime.strptime(app.data_termino.get(), '%d-%m-%Y')
    d1 = datetime.strptime(app.data_inicial.get(), '%d-%m-%Y')
    quantidade_dias = abs((d2 - d1).days)  # quantidade de dias total do anuncio
  
    valor_investido = quantidade_dias * float(app.invest_por_dia.get())  # valor total investido no anuncio
    visualizacoes = valor_investido * 30 # Visualizações do anúncio original
    alcance_max = visualizacoes
    ctr = 0.12 # Click Through rate: cliques recebidos pelo seu anúncio dividido pelo número de vezes que ele foi visualizado
    cliques_max = 0
    compartilhamentos_max = 0

    # Calcula visualizações do anúncio (anúncio original + 4 compartilhamentos)
    for _ in range(4):
        cliques = visualizacoes * ctr
        cliques_max += cliques
        compartilhamentos = cliques * 0.15 
        compartilhamentos_max += compartilhamentos
        visualizacoes = compartilhamentos * 40 # 40 novas visualizações geradas a cada compartilhamento
        alcance_max += visualizacoes

    return f"""
    Anúncio: {app.nome_anuncio.get()}
    Cliente: {app.nome_cliente.get()}
    Valor total investido: R${valor_investido}
    Quantidade máxima de visualizações: {round(alcance_max)}
    Quantidade máxima de cliques: {round(cliques_max)}
    Quantidade máxima de compartilhamentos: {round(compartilhamentos_max)}
    """

def selecionar_anuncio(event):
    global selected
    index = app.anuncios_lista.curselection()[0]
    selected = app.anuncios_lista.get(index)
    app.nome_anuncio_entry.delete(0, END)
    app.nome_anuncio_entry.insert(END, selected[1])
    app.nome_cliente_entry.delete(0, END)
    app.nome_cliente_entry.insert(END, selected[2])
    app.data_inicial_entry.delete(0, END)
    app.data_inicial_entry.insert(END, selected[3])
    app.data_termino_entry.delete(0, END)
    app.data_termino_entry.insert(END, selected[4])
    app.invest_por_dia_entry.delete(0, END)
    app.invest_por_dia_entry.insert(END, selected[5])
    return selected

# Função buscar anuncio não finalizada
# def buscar_anuncio():
#     app.anuncios_lista.delete(0, END)
#     rows = core.search(app.nome_cliente.get())
#     for r in rows:
#         app.anuncios_lista.insert(END, r)

if __name__ == "__main__":
    app = interface()
    app.anuncios_lista.bind('<<ListboxSelect>>', selecionar_anuncio)

    app.cadastrar_botao.configure(command=cadastrar)
    app.atualizar_botao.configure(command=atualizar)
    app.ver_todos_botao.configure(command=visualizar)
    app.deletar_botao.configure(command=deletar)
    app.relatorio_botao.configure(command=gerar_relatorio)
    #app.buscar_botao.configure(command=buscar_anuncio)
  

    app.run()
