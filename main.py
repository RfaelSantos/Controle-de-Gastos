from tkinter import *

'''Tela principal'''
window = Tk()
window.title('Controle de Gastos')
window.geometry("400x400")
window.config(padx=50, pady=50)

add_button = Button(text='Novo Gasto', width=10)
add_button.grid(column=1, row=1)

alt_button = Button(text='Alterar', width=10)
alt_button.grid(column=2, row=1)

del_button = Button(text='Excluir', width=10)
del_button.grid(column=3, row=1)

window.mainloop()