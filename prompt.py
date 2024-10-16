import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# Função para cadastrar um doador
def cadastrar_doador():
    # Função para salvar o doador no banco de dados
    def salvar_doador():
        cpf = int(entry_cpf.get())
        nome = entry_nome.get()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                database="cdl"
            )

            cursor = conn.cursor()
            cursor.execute("INSERT INTO doador (cpf, nome, doacoes) VALUES (%s, %s, 0)", (cpf, nome))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Sucesso", "Doador cadastrado com sucesso.")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar o doador: {err}")

    # Configuração da interface gráfica para cadastro de doador
    cadastro_doador_window = tk.Toplevel(root)
    cadastro_doador_window.title("Cadastro de Doador")

    label_cpf = tk.Label(cadastro_doador_window, text="CPF:")
    label_cpf.grid(row=0, column=0, padx=10, pady=5)
    entry_cpf = tk.Entry(cadastro_doador_window)
    entry_cpf.grid(row=0, column=1, padx=10, pady=5)

    label_nome = tk.Label(cadastro_doador_window, text="Nome:")
    label_nome.grid(row=1, column=0, padx=10, pady=5)
    entry_nome = tk.Entry(cadastro_doador_window)
    entry_nome.grid(row=1, column=1, padx=10, pady=5)

    btn_salvar = tk.Button(cadastro_doador_window, text="Salvar", command=salvar_doador)
    btn_salvar.grid(row=2, column=0, columnspan=2, pady=10)

# Função para cadastrar uma doação
def cadastrar_doacao():
    # Função para salvar a doação no banco de dados
    def salvar_doacao():
        nome_produto = entry_nome_produto.get()
        quantidade = int(entry_quantidade.get())
        tipo_produto = entry_tipo_produto.get()
        descricao_produto = entry_descricao_produto.get()
        cpf_doador = int(entry_cpf_doador.get())

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                database="cdl"
            )

            cursor = conn.cursor()
            cursor.execute("INSERT INTO doacao (nome_produto, quantidade, tipo_produto, descricao_produto, cpf_doador) "
                           "VALUES (%s, %s, %s, %s, %s)",
                           (nome_produto, quantidade, tipo_produto, descricao_produto, cpf_doador))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Sucesso", "Doação cadastrada com sucesso.")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar a doação: {err}")

    # Configuração da interface gráfica para cadastro de doação
    cadastro_doacao_window = tk.Toplevel(root)
    cadastro_doacao_window.title("Cadastro de Doação")

    label_nome_produto = tk.Label(cadastro_doacao_window, text="Nome do Produto:")
    label_nome_produto.grid(row=0, column=0, padx=10, pady=5)
    entry_nome_produto = tk.Entry(cadastro_doacao_window)
    entry_nome_produto.grid(row=0, column=1, padx=10, pady=5)

    label_quantidade = tk.Label(cadastro_doacao_window, text="Quantidade:")
    label_quantidade.grid(row=1, column=0, padx=10, pady=5)
    entry_quantidade = tk.Entry(cadastro_doacao_window)
    entry_quantidade.grid(row=1, column=1, padx=10, pady=5)

    label_tipo_produto = tk.Label(cadastro_doacao_window, text="Tipo do Produto:")
    label_tipo_produto.grid(row=2, column=0, padx=10, pady=5)
    entry_tipo_produto = tk.Entry(cadastro_doacao_window)
    entry_tipo_produto.grid(row=2, column=1, padx=10, pady=5)

    label_descricao_produto = tk.Label(cadastro_doacao_window, text="Descrição do Produto:")
    label_descricao_produto.grid(row=3, column=0, padx=10, pady=5)
    entry_descricao_produto = tk.Entry(cadastro_doacao_window)
    entry_descricao_produto.grid(row=3, column=1, padx=10, pady=5)

    label_cpf_doador = tk.Label(cadastro_doacao_window, text="CPF do Doador:")
    label_cpf_doador.grid(row=4, column=0, padx=10, pady=5)
    entry_cpf_doador = tk.Entry(cadastro_doacao_window)
    entry_cpf_doador.grid(row=4, column=1, padx=10, pady=5)

    btn_salvar = tk.Button(cadastro_doacao_window, text="Salvar", command=salvar_doacao)
    btn_salvar.grid(row=5, column=0, columnspan=2, pady=10)

# Função para cadastrar um beneficiado
def cadastrar_beneficiado():
    # Função para salvar o beneficiado no banco de dados
    def salvar_beneficiado():
        cpf = int(entry_cpf_beneficiado.get())
        nome = entry_nome_beneficiado.get()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                database="cdl"
            )

            cursor = conn.cursor()
            cursor.execute("INSERT INTO beneficiado (cpf, nome) VALUES (%s, %s)", (cpf, nome))
            conn.commit()
            cursor.close()
            conn.close()

            messagebox.showinfo("Sucesso", "Beneficiado cadastrado com sucesso.")

        except mysql.connector.Error as err:
            messagebox.showerror("Erro", f"Erro ao cadastrar o beneficiado: {err}")

    # Configuração da interface gráfica para cadastro de beneficiado
    cadastro_beneficiado_window = tk.Toplevel(root)
    cadastro_beneficiado_window.title("Cadastro de Beneficiado")

    label_cpf_beneficiado = tk.Label(cadastro_beneficiado_window, text="CPF:")
    label_cpf_beneficiado.grid(row=0, column=0, padx=10, pady=5)
    entry_cpf_beneficiado = tk.Entry(cadastro_beneficiado_window)
    entry_cpf_beneficiado.grid(row=0, column=1, padx=10, pady=5)

    label_nome_beneficiado = tk.Label(cadastro_beneficiado_window, text="Nome:")
    label_nome_beneficiado.grid(row=1, column=0, padx=10, pady=5)
    entry_nome_beneficiado = tk.Entry(cadastro_beneficiado_window)
    entry_nome_beneficiado.grid(row=1, column=1, padx=10, pady=5)

    btn_salvar_beneficiado = tk.Button(cadastro_beneficiado_window, text="Salvar", command=salvar_beneficiado)
    btn_salvar_beneficiado.grid(row=2, column=0, columnspan=2, pady=10)

# Função para visualizar doações
def visualizar_doacoes():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            database="cdl"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM doacao")
        doacoes = cursor.fetchall()

        # Exibir as doações
        doacoes_table_window = tk.Toplevel(root)
        doacoes_table_window.title("Doações")

        headers = ['ID Doação', 'Nome Produto', 'Quantidade', 'Tipo Produto', 'Descrição Produto', 'CPF Doador']
        tree = ttk.Treeview(doacoes_table_window, columns=headers, show='headings')
        for col in headers:
            tree.heading(col, text=col)

        for doacao in doacoes:
            tree.insert("", "end", values=doacao)

        tree.pack(expand=True, fill='both')

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao buscar as doações: {err}")


# Função para visualizar beneficiados
def visualizar_beneficiados():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            database="cdl"
        )

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM beneficiado")
        beneficiados = cursor.fetchall()

        # Exibir os beneficiados
        beneficiados_table_window = tk.Toplevel(root)
        beneficiados_table_window.title("Beneficiados")

        headers = ['CPF Beneficiado', 'Nome Beneficiado']
        tree = ttk.Treeview(beneficiados_table_window, columns=headers, show='headings')
        for col in headers:
            tree.heading(col, text=col)

        for beneficiado in beneficiados:
            tree.insert("", "end", values=beneficiado)

        tree.pack(expand=True, fill='both')

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao buscar os beneficiados: {err}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Casa do Leo")

# Estilo para ttk
style = ttk.Style()

# Cores
cor_fundo = "#FFFFFF"
cor_banner = "#FFC107"  # Amarelo
cor_botao = "#4CAF50"   # Verde
cor_borda_botao = "#388E3C"  # Verde mais escuro
cor_texto = "#333333"

# Configurações de cores
root.configure(bg=cor_fundo)
style.configure("TButton", padding=(10, 5, 10, 5), font=('Arial', 10, 'bold'), background='#444', foreground='#444', relief="flat", borderwidth=2)

# Container para os botões e imagem
container = tk.Frame(root, bg=cor_fundo)
container.pack(side="top", fill="both", padx=0, pady=0)

# Adicione a imagem ao Canvas
width = 70  # Largura desejada
height = 70  # Altura desejada
canvas = tk.Canvas(container, width=width, height=height, bg=cor_fundo, highlightthickness=0)
canvas.pack(side="left", padx=10,pady=10)

# Botões alinhados em linha
btn_cadastrar_doador = ttk.Button(container, text="Cadastrar Doador", command=cadastrar_doador, style="TButton", cursor="hand2")
btn_cadastrar_doador.pack(side="right", padx=10)

btn_cadastrar_doacao = ttk.Button(container, text="Cadastrar Doação", command=cadastrar_doacao, style="TButton", cursor="hand2")
btn_cadastrar_doacao.pack(side="right", padx=10)

btn_cadastrar_beneficiado = ttk.Button(container, text="Cadastrar Beneficiado", command=cadastrar_beneficiado, style="TButton", cursor="hand2")
btn_cadastrar_beneficiado.pack(side="right", padx=10)

btn_visualizar_doacoes = ttk.Button(container, text="Visualizar Doações", command=visualizar_doacoes, style="TButton", cursor="hand2")
btn_visualizar_doacoes.pack(side="right", padx=10)

btn_visualizar_beneficiados = ttk.Button(container, text="Visualizar Beneficiados", command=visualizar_beneficiados, style="TButton", cursor="hand2")
btn_visualizar_beneficiados.pack(side="right", padx=10)

# Banner
banner = tk.Label(root, bg=cor_banner, fg=cor_fundo, font=('arial', 20, 'bold'), pady=10)
banner.pack(fill="x")

# Define o tamanho inicial da janela
largura_janela = 800
altura_janela = 600
root.geometry(f"{largura_janela}x{altura_janela}+{int((largura_janela / 2) - (largura_janela / 2))}+{int((altura_janela / 2) - (altura_janela / 2))}")

# Maximiza a janela
root.state("zoomed")

# Texto informativo
texto_informativo = """"Faça todo o bem que puder, com todos os meios que puder, de todas as maneiras que puder, em todos os lugares que puder, em todos os momentos que puder, para todas as pessoas que puder, enquanto você puder." - São João Batista de La Salle
"""

# Caixa de texto informativa
caixa_texto = tk.Label(root, text=texto_informativo, font=('Helvetica', 12), bg=cor_fundo, fg=cor_texto, wraplength=600, justify="left")
caixa_texto.pack(side="left", padx=20)

# Inicializa a interface gráfica
root.mainloop()
