# -*- coding: utf-8 -*-
#
# Desafio de Programação Capgemini (2021) 
# 1ª Parte - Calculadora de alcance de anúncio online.
#
# O código calcula uma projeção aproximada da quantidade máxima de pessoas 
# que visualizarão o mesmo anúncio (anúncio original + compartilhamentos),
# considerando o valor em reais investido.
#
# Autora: Ana Larissa Dias - larissa.engcomp@gmail.com
# Junho 2021

import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import messagebox


def calcula_alcance():
        try:
            valor_investido = investimento_input.get()
            visualizacoes = float(valor_investido) * 30 # Visualizações do anúncio original
            alcance_max = visualizacoes
            ctr = 0.12 # Click Through rate: cliques recebidos pelo seu anúncio dividido pelo número de vezes que ele foi visualizado

            # Calcula visualizações do anúncio (anúncio original + 4 compartilhamentos)
            for _ in range(4):
                cliques = visualizacoes * ctr  
                compartilhamentos = cliques * 0.15 # 
                visualizacoes = compartilhamentos * 40 # 40 novas visualizações geradas a cada compartilhamento
                alcance_max += visualizacoes
      
            resultado["text"] = f"""O anúncio terá aproximadamente 
{round(alcance_max)} visualizações"""
        except ValueError:
            messagebox.showerror("Erro", "Por favor insira um valor válido. O valor inserido não pode conter vírgulas, espaços ou caracteres.", justify=CENTER)
    
    

# Cria a janela principal da calculadora
window = tk.Tk()
window.geometry("305x300")
window.title("Calculadora de Alcance")
window.rowconfigure(4, minsize=80, weight=1)
window.columnconfigure(1, minsize=100, weight=1)
labelFont1 = tkFont.Font(family="calibre", size=12, weight="bold")

# Cria o Widget de caixa de texto para entrada do valor investido
investimento_frame = tk.Frame(master=window)
investimento_texto = tk.Label(master=investimento_frame, text="Valor investido (R$):", font=labelFont1)
investimento_input = tk.Entry(master=investimento_frame, width=23)


# Define o layout do Widget de caixa de texto para entrada do valor investido 
investimento_input.grid(row=4, column=0, padx=10, pady=10) #, sticky="nsew")#, sticky="w")
investimento_texto.grid(row=3, column=0, padx=10, pady=10) #, sticky="nsew")#, sticky="w")

# Cria o botão calcular que chama a função calcula_alcance() e mostra o resultado
botao_calcular = tk.Button(
    master=window,
    text="Calcular", font=labelFont1,
    command=calcula_alcance
)
resultado = tk.Label(master=window, font=('calibre',11,'bold'), justify=CENTER) #, text="visualizações")

# Define o layout da aplicação
investimento_frame.grid(row=1, column=1, padx=10, pady=10) 
botao_calcular.grid(row=2, column=1, padx=10, pady=10)
resultado.grid(row=3, column=1, padx=10, pady=10, sticky="nsew") 

# Roda a aplicação
window.mainloop()
