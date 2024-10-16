import tkinter as tk
from tkinter import messagebox

# Função para adicionar o item à lista e salvar no arquivo
def adicionar_item():
    item = entry_item.get()
    quantidade = entry_quantidade.get()
    departamento = entry_departamento.get()

    if item and quantidade and departamento:
        with open("lista_compras.txt", "a") as file:
            file.write(f"Item: {item}, Quantidade: {quantidade}, Departamento: {departamento}\n")
        
        # Limpar as entradas
        entry_item.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)
        entry_departamento.delete(0, tk.END)

        messagebox.showinfo("Sucesso", "Item adicionado à lista de compras!")
    else:
        messagebox.showwarning("Erro", "Todos os campos são obrigatórios!")

# Criar a janela principal
janela = tk.Tk()
janela.title("Lista de Compras")

# Configurar a interface
tk.Label(janela, text="Item:").grid(row=0, column=0, padx=10, pady=5)
entry_item = tk.Entry(janela)
entry_item.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Quantidade:").grid(row=1, column=0, padx=10, pady=5)
entry_quantidade = tk.Entry(janela)
entry_quantidade.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Departamento:").grid(row=2, column=0, padx=10, pady=5)
entry_departamento = tk.Entry(janela)
entry_departamento.grid(row=2, column=1, padx=10, pady=5)

# Botão para adicionar o item
btn_adicionar = tk.Button(janela, text="Adicionar à lista", command=adicionar_item)
btn_adicionar.grid(row=3, column=0, columnspan=2, pady=10)

# Executar a janela principal
janela.mainloop()