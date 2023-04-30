import tkinter
from tkinter import *
from tkinter import ttk
import pyodbc
import pandas as pd

Server = 'LAPTOP-0O4DDNV9\SQLEXPRESS'
conexao = pyodbc.connect(Driver='{SQL Server}', host=Server)
gastos = conexao.execute("SELECT * FROM [Controle_Gastos].[dbo].[Gasto]")
print(gastos)

'''Tela principal'''
window = Tk()
window.title('Controle de Gastos')
window.geometry("400x400")
window.config(padx=50, pady=50)

add_button = Button(text='Novo Gasto', width=10)
add_button.grid(column=1, row=1)

alt_button = Button(text='Alterar', width=10)
alt_button.grid(column=1, row=2)

del_button = Button(text='Excluir', width=10)
del_button.grid(column=1, row=3)

tree = ttk.Treeview(window, selectmode="browse", columns=('column1', 'column2', 'column3'), show="headings")
tree.column("column1", width=100, minwidth=10, stretch=NO, anchor='c')
tree.heading("#1", text='Descrição')
tree.column("column2", width=100, minwidth=10, stretch=NO, anchor='c')
tree.heading("#2", text='Valor')
tree.column("column3", width=100, minwidth=10, stretch=NO, anchor='c')
tree.heading("#3", text='Tipo')
tree.grid(column=1, row=4)

for i in gastos:
    tree.insert("", 'end', iid=i[0], values=(i[2], i[1], i[3]))


window.mainloop()