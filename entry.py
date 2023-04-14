from tkinter import *
from tkinter import ttk, messagebox

def save():
    valor = valor_input.get()
    desc = desc_input.get()
    tipo = combo.get()
    messagebox.showinfo('Ok', message='Gasto Adicionado com Sucesso!')


'''Configuração da janela'''
options = [
    "Conta de Consumo",
    "Alimentação",
    "Roupas",
    "Sapatos",
    "Lazer",
    "Viagem",
    "Outros"
]


entry_window = Tk()
entry_window.title('Novo Gasto')
entry_window.geometry("400x400")
entry_window.config(padx=50, pady=50)

valor_label = Label(text='Valor: ', height=2)
valor_label.grid(column=0, row=2)
desc_label = Label(text='Descrição:', height=2)
desc_label.grid(column=0, row=1)
inv_label = Label(height=1)
inv_label.grid(column=0, row=4)

valor_input = Entry(width=30)
valor_input.grid(column=1, row=2, sticky="W")
desc_input = Entry(width=30)
desc_input.grid(column=1, row=1, sticky="EW")

combo = ttk.Combobox(state="readonly",values = ["Conta de Consumo","Alimentação",
                                                "Roupas","Sapatos","Lazer","Viagem","Outros"])
combo.grid(column=1, row=3)


add_button = Button(text='Salvar', width=30, command=save)
add_button.grid(column=1, row=5)

entry_window.mainloop()
