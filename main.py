from tkinter import *
from tkinter import ttk, messagebox
import pyodbc

'''Conexão com o Banco de Dados'''
Server = 'LAPTOP-0O4DDNV9\SQLEXPRESS'
conexao = pyodbc.connect(Driver='{SQL Server}', host=Server)
gastos = conexao.execute("SELECT * FROM [Controle_Gastos].[dbo].[Gasto]")


'''Função Save para inclusão dos registros no Banco de Dados'''
def save():

    def insert():
        valor = valor_input.get()
        desc = desc_input.get()
        tipo = combo.get()

        conexao.execute(
            f"INSERT INTO [Controle_Gastos].[dbo].[Gasto](valor, descricao, tipo) VALUES ('{valor}','{desc}', '{tipo}')")
        conexao.commit()
        messagebox.showinfo('Ok', message='Gasto Adicionado com Sucesso!')
        insertWindow.destroy()

    insertWindow = Toplevel(window)
    insertWindow.title('Novo Gasto')
    insertWindow.geometry("400x400")
    insertWindow.config(padx=50, pady=20)

    valor_label = Label(insertWindow, text='Valor: ', height=2)
    valor_label.grid(column=0, row=2)
    desc_label = Label(insertWindow, text='Descrição: ', height=2)
    desc_label.grid(column=0, row=1)
    inv_label = Label(insertWindow, height=1)
    inv_label.grid(column=0, row=4)

    valor_input = Entry(insertWindow, width=30)
    valor_input.grid(column=1, row=2, sticky="W")
    desc_input = Entry(insertWindow, width=30)
    desc_input.grid(column=1, row=1, sticky="EW")

    combo = ttk.Combobox(insertWindow, state="readonly", values=["Conta de Consumo", "Alimentação",
                                                   "Roupas", "Sapatos", "Lazer", "Viagem", "Outros"])
    combo.grid(column=1, row=3)

    add_button = Button(insertWindow, text='Salvar', width=30, command=insert)
    add_button.grid(column=1, row=5)

    insertWindow.grid()


'''Função Delete para exclusão do registro posicionado no Banco de Dados'''
def delete():
    id = tree.selection()[0]

    confirmacao = messagebox.askokcancel(title="Confirmação", message="Tem certeza que deseja apagar o registro?")

    if confirmacao:
        conexao.execute(f"DELETE FROM [Controle_Gastos].[dbo].[Gasto] WHERE id = '{id}'" )
        conexao.commit()

        messagebox.showinfo(message="Registro deletado com sucesso!")
        tree.delete(id)


'''Função Update para alteração do registro posicionado no Banco de Dados'''
def update():

    def upd():
        id = tree.selection()[0]
        upd_valor = upd_valor_input.get()
        upd_desc = upd_desc_input.get()
        upd_tipo = upd_combo.get()

        conexao.execute(
            f"UPDATE [Controle_Gastos].[dbo].[Gasto] SET valor='{upd_valor}',descricao='{upd_desc}',tipo='{upd_tipo}' WHERE id='{id}'"
        )
        conexao.commit()
        messagebox.showinfo('Ok', message='Gasto Alterado com Sucesso!')

        upd_valor_input.insert(0, '')
        upd_desc_input.insert(0, '')
        updateWindow.destroy()

    id = tree.selection()[0]
    row_to_list = []
    updateWindow = Toplevel(window)
    updateWindow.title("Alteração")
    updateWindow.geometry("400x400")
    updateWindow.config(padx=50, pady=20)

    gastos = conexao.execute(f"SELECT * FROM [Controle_Gastos].[dbo].[Gasto] WHERE id = '{id}'")

    for row in gastos:
        row_to_list = [elem for elem in row]

    upd_valor_label = Label(updateWindow, text='Valor: ', height=2)
    upd_valor_label.grid(column=0, row=2)
    upd_desc_label = Label(updateWindow, text='Descrição: ', height=2)
    upd_desc_label.grid(column=0, row=1)
    upd_inv_label = Label(updateWindow, height=1)
    upd_inv_label.grid(column=0, row=4)

    upd_valor_input = Entry(updateWindow, width=30)
    upd_valor_input.insert(0, row_to_list[1])
    upd_valor_input.grid(column=1, row=2, sticky="W")
    upd_desc_input = Entry(updateWindow, width=30)
    upd_desc_input.insert(0, row_to_list[2])
    upd_desc_input.grid(column=1, row=1, sticky="EW")

    upd_combo = ttk.Combobox(updateWindow, state="readonly", values=["Conta de Consumo", "Alimentação",
                                                   "Roupas", "Sapatos", "Lazer", "Viagem", "Outros"])
    upd_combo.grid(column=1, row=3)

    upd_button = Button(updateWindow, text='Salvar', width=30, command=upd)
    upd_button.grid(column=1, row=5)

    updateWindow.grid()


'''Montagem de Tela'''
window = Tk()
window.title('Controle de Gastos')
window.geometry("400x400")
window.config(padx=50, pady=20)

add_button = Button(text='Novo Gasto', width=10, command=save)
add_button.grid(column=1, row=1, pady=5)
alt_button = Button(window, text='Alterar', width=10, command=update)
alt_button.grid(column=1, row=2, pady=5)
del_button = Button(text='Excluir', width=10, command=delete)
del_button.grid(column=1, row=3, pady=5)


'''TreeView com os registros inseridos no Banco de Dados'''
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
tree.selection()

window.mainloop()
