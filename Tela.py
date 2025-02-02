import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from algoritimos import *
from algoritimos import Item
import datetime
import tkinter.messagebox as messagebox


class Application(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.configure(fg_color="#a9a9a9")
        self.geometry("800x600")
        self.iconbitmap("D:/MilhasGerais/MG.ico")
        self.title("MILHAS GERAIS")

        self.fontePadrao = ("Arial", 12)

        self.tela_login = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)
        self.primeira_tela = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)
        self.resgistrar = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)
        self.lista = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)
        self.emprestar = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)
        self.listaEmpretimo = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)
        self.cadatro = ctk.CTkFrame(self, fg_color="#a9a9a9", width=800, height=600)

        self.Create_tela()
        self.tela_login.pack()

    def Create_tela(self):
        # Tela Login
        self.Central_frame = ctk.CTkFrame(self.tela_login, fg_color="#504B4B", width=400, height=300)
        self.Central_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.top_frame = ctk.CTkFrame(self.tela_login, fg_color="#a9a9a9", width=800, height=100)
        self.top_frame.place(x=0, y=0)

        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top_frame, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)

        self.entry_username = ctk.CTkEntry(self.Central_frame, placeholder_text="Login", width=280,height=40)
        self.entry_username.place(relx=0.15, rely=0.2)

        self.entry_password = ctk.CTkEntry(self.Central_frame, show="*", placeholder_text="Senha", width=280,height=40)
        self.entry_password.place(relx=0.15, rely=0.4)

        button_login = ctk.CTkButton(self.Central_frame, text="Login", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, command=self.Login)
        button_login.place(relx=0.05, rely=0.8)

        button_register = ctk.CTkButton(self.Central_frame, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, command= self.show_cadastro)
        button_register.place(relx=0.605, rely=0.8)
        
        #tela de cadastros
        
        self.Central_frame5 = ctk.CTkFrame(self.cadatro, fg_color="#504B4B", width=500, height=400)
        self.Central_frame5.place(relx=0.5, rely=0.5, anchor="center")

        self.top_frame5 = ctk.CTkFrame(self.cadatro, fg_color="#a9a9a9", width=800, height=100)
        self.top_frame5.place(x=0, y=0)
        
        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top_frame5, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)
        
        self.entry_login = ctk.CTkEntry(self.Central_frame5, placeholder_text="Login", width=280,height=40)
        self.entry_login.place(relx=0.15, rely=0.2)

        self.entry_user = ctk.CTkEntry(self.Central_frame5, placeholder_text="Nome", width=280,height=40)
        self.entry_user.place(relx=0.15, rely=0.4)
        
        self.entry_pass = ctk.CTkEntry(self.Central_frame5, show="*", placeholder_text="Senha", width=280,height=40)
        self.entry_pass.place(relx=0.15, rely=0.6)
        
        self.entry_pass2 = ctk.CTkEntry(self.Central_frame5, show="*", placeholder_text="confirmar a senha", width=280,height=40)
        self.entry_pass2.place(relx=0.15, rely=0.8)
        
        button_cadastrar = ctk.CTkButton(self.cadatro, text="Cadastrar", fg_color="#C50F11", hover_color='darkred', width=200, height=40, font=self.fontePadrao, command= self.cadastrar_usuario)
        button_cadastrar.place(relx=0.74, rely=0.9)

        button_voltar = ctk.CTkButton(self.cadatro, text="Voltar", fg_color="#C50F11", hover_color='darkred',  width=200, height=40,font=self.fontePadrao,command=self.voltar_login)
        button_voltar.place(relx=0.01, rely=0.9)
        
        # Tela Principal
        self.top0_frame = ctk.CTkFrame(self.primeira_tela, fg_color="#a9a9a9", width=800, height=100)

        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top0_frame, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)

        botao_registrar = ctk.CTkButton(self.primeira_tela, text="Registrar Item", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, width=200, height=40, command=self.show_registar)
        botao_registrar.place(relx=0.1, rely=0.3)
        botao_lista = ctk.CTkButton(self.primeira_tela, text="Lista de Itens", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, width=200, height=40, command=self.show_lista)
        botao_lista.place(relx=0.1, rely=0.5)
        botao_emprestar = ctk.CTkButton(self.primeira_tela, text="Emprestar Item", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, width=200, height=40, command=self.show_emprestimo)
        botao_emprestar.place(relx=0.1, rely=0.7)

        # Tela Registrar
        self.top1_frame = ctk.CTkFrame(self.resgistrar, fg_color="#a9a9a9", width=800, height=100)

        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top1_frame, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)

       
        self.nome = ctk.CTkEntry(self.resgistrar, width=250,placeholder_text="Nome do Item", font=self.fontePadrao)
        self.nome.pack(side=ctk.LEFT)

        qtdlabel = ctk.CTkLabel(self.resgistrar, text="Quantidade", fg_color="#a9a9a9", font=self.fontePadrao)
        qtdlabel.pack(side=ctk.LEFT)
        self.qtd = ttk.Combobox(self.resgistrar, width=5, values=list(range(1, 100)), font=self.fontePadrao)
        self.qtd.current(0)
        self.qtd.pack(side=ctk.LEFT)

        registrar = ctk.CTkButton(self.resgistrar, text="Registrar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.adiciona_item)
        registrar.place(relx=0.74, rely=0.9)

        voltar = ctk.CTkButton(self.resgistrar, text="Voltar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.voltar_mainscren)
        voltar.place(relx=0.01, rely=0.9)

        # Tela Lista
        self.frame = ctk.CTkFrame(self.lista, width=800, height=600, fg_color="#a9a9a9")
        self.top2_frame = ctk.CTkFrame(self.lista, fg_color="#a9a9a9", width=800, height=100)

        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top2_frame, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)

        self.create_table(self.frame, "estoque.txt")

        self.entry_busca = ctk.CTkEntry(self.lista, width=500, placeholder_text="Buscar")
        self.entry_busca.place(relx=0.2, rely=0.24)

        espaco = ctk.CTkFrame(self.lista, height=10, fg_color="#a9a9a9")
        espaco.pack()

        self.qtd_ret = ttk.Combobox(self.frame, width=5, values=list(range(1, 100)), font=self.fontePadrao)
        self.qtd_ret.current(0)
        self.qtd_ret.pack(side=tk.LEFT)
        retirar = ctk.CTkButton(self.frame, text="Retirar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=50, height=30, command=self.remove_item)
        retirar.pack(side=ctk.LEFT, padx=1)

        voltar = ctk.CTkButton(self.lista, text="Voltar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.voltar_mainscren)
        voltar.place(relx=0.01, rely=0.9)

        buscar = ctk.CTkButton(self.lista, text="Buscar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.buscar_item)
        buscar.place(relx=0.74, rely=0.9)

        # Tela Emprestimo
        self.top3_frame = ctk.CTkFrame(self.emprestar, fg_color="#a9a9a9", width=800, height=100)

        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top3_frame, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)

        self.entry_item = ctk.CTkEntry(self.emprestar, placeholder_text="Item", width=350, height=50)
        self.entry_item.place(relx=0.01, rely=0.3)
        self.entry_qtd = ttk.Combobox(self.emprestar, width=10, values=list(range(1, 100)), font=self.fontePadrao)
        self.entry_qtd.place(relx=0.45, rely=0.3)
        self.entry_nome = ctk.CTkEntry(self.emprestar, placeholder_text="Emprestador", width=350, height=50)
        self.entry_nome.place(relx=0.01, rely=0.4)
        self.entry_nome2 = ctk.CTkEntry(self.emprestar, placeholder_text="Emprestado para", width=350, height=50)
        self.entry_nome2.place(relx=0.01, rely=0.5)
        lista_emprestimo = ctk.CTkButton(self.emprestar, text="Lista de Itens", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, width=200, height=40,command=self.show_listaEmpretimo)
        lista_emprestimo.place(relx=0.74, rely=0.9)

        voltar = ctk.CTkButton(self.emprestar, text="Voltar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.voltar_mainscren)
        voltar.place(relx=0.01, rely=0.9)

        botao_registro = ctk.CTkButton(self.emprestar, text="Emprestar Item", fg_color="#C50F11", hover_color='darkred', font=self.fontePadrao, width=200, height=40,command=self.registra_emprestimo)
        botao_registro.place(relx=0.74, rely=0.5)
        
        #lista emprestimo
        self.top_frame7 = ctk.CTkFrame(self.listaEmpretimo, fg_color="#a9a9a9", width=800, height=100)
        
        
        imagem = tk.PhotoImage(file="D:/MilhasGerais/MG.png")
        label_imagem = ctk.CTkLabel(self.top_frame7, image=imagem, text="")
        label_imagem.pack(padx=10, pady=10, side=ctk.LEFT)
        
        self.frame1 = ctk.CTkFrame(self.listaEmpretimo, width=800, height=600, fg_color="#a9a9a9")
        
        self.create_emprestimo_table()
        
        devolver = ctk.CTkButton(self.listaEmpretimo, text="Devolver", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.devolver_item)
        devolver.place(relx=0.74, rely=0.9)
        
        voltar = ctk.CTkButton(self.listaEmpretimo, text="Voltar", font=self.fontePadrao, fg_color="#C50F11", hover_color='darkred', width=200, height=40, command=self.voltar_emprestimo)
        voltar.place(relx=0.01, rely=0.9)

    def show_primeiraTela(self):
        self.tela_login.pack_forget()
        self.primeira_tela.pack(fill="both", expand=True)
        self.top0_frame.place(x=0, y=0)

    def show_registar(self):
        self.primeira_tela.pack_forget()
        self.resgistrar.pack(fill="both", expand=True)
        self.top1_frame.place(x=0, y=0)

    def show_lista(self):
        self.primeira_tela.pack_forget()
        self.lista.pack(fill="both", expand=True)
        self.frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.top2_frame.place(x=0, y=0)

    def show_emprestimo(self):
        self.primeira_tela.pack_forget()
        self.emprestar.pack(fill="both", expand=True)
        self.top3_frame.place(x=0, y=0)

    def show_listaEmpretimo(self):
        self.emprestar.pack_forget()
        self.listaEmpretimo.pack(fill="both", expand=True)
        self.frame1.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
        self.top_frame7.place(x=0, y=0)
        
    def show_cadastro(self):
        self.tela_login.pack_forget()
        self.cadatro.pack(fill="both", expand=True)
      
        
    def voltar_emprestimo(self):
        self.listaEmpretimo.pack_forget()
        self.emprestar.pack(fill="both", expand=True)
        
    def voltar_mainscren(self):
        self.resgistrar.pack_forget()
        self.lista.pack_forget()
        self.emprestar.pack_forget()
        self.primeira_tela.pack(fill="both", expand=True)
        
    def voltar_login(self):
        self.cadatro.pack_forget()
        self.tela_login.pack(fill="both", expand=True)

    def adiciona_item(self):
        new_item = Item(self.nome.get(), self.qtd.get())
        adicionar_item(new_item)
        self.atualizar_tabela()

    def cadastrar_usuario(self):
        if (self.entry_pass.get() == self.entry_pass2.get()):
            novo_usuario = Usuario(self.entry_login.get(),self.entry_pass.get(),self.entry_user.get())
            cadastra_usuario(novo_usuario)
        else:
            messagebox.showerror("Erro", "Senhas diferentes")
    
    def Login(self):
        user = Usuario(self.entry_username.get(),self.entry_password.get(),"")
        autenticar = autenticar_usuario(user)
        
        if autenticar:
            self.show_primeiraTela()
        else:
            messagebox.showerror("Erro", "Login ou senha errada")
            
    
    
            
    def create_table(self, frame, arquivo):
        dados = ler_estoque(arquivo)

        self.table = ttk.Treeview(frame)
        self.table['columns'] = ('produto', 'quantidade')

        self.table.column("#0", width=150)  # ID
        self.table.column('produto', width=300)
        self.table.column('quantidade', width=200)

        self.table.heading("#0", text='ID')
        self.table.heading('produto', text='Produto')
        self.table.heading('quantidade', text='Quantidade')

        for i, (produto, quantidade) in enumerate(dados, start=1):
            self.table.insert(parent='', index='end', iid=i, text=str(i), values=(produto, quantidade))

        self.table.pack(expand=True, fill='both')

    def atualizar_tabela(self):
        for item in self.table.get_children():
            self.table.delete(item)

        dados = ler_estoque('estoque.txt')

        for i, (produto, quantidade) in enumerate(dados, start=1):
            self.table.insert(parent='', index='end', iid=i, text=str(i), values=(produto, quantidade))
    def remove_item(self):
        item_selecionado = self.table.selection()

        if item_selecionado:
            nome_item = self.table.item(item_selecionado[0])['values'][0]
            quantidade_a_retirar = int(self.qtd_ret.get())
            item = Item(nome_item,quantidade_a_retirar)
            
            remover_item(item)
            self.atualizar_tabela()

            
           
    def create_emprestimo_table(self):
        self.emprestimo_frame = ctk.CTkFrame(self.listaEmpretimo, width=500, height=400, fg_color="#a9a9a9")

        self.emprestimo_table = ttk.Treeview(self.emprestimo_frame)
        self.emprestimo_table['columns'] = ('item', 'quantidade', 'emprestador', 'emprestado_para', 'data_emprestimo')

        self.emprestimo_table.column("#0", width=50)  # ID
        self.emprestimo_table.column('item', width=100)
        self.emprestimo_table.column('quantidade', width=50)
        self.emprestimo_table.column('emprestador', width=100)
        self.emprestimo_table.column('emprestado_para', width=100)
        self.emprestimo_table.column('data_emprestimo', width=100)

        self.emprestimo_table.heading("#0", text='ID')
        self.emprestimo_table.heading('item', text='Item')
        self.emprestimo_table.heading('quantidade', text='Quantidade')
        self.emprestimo_table.heading('emprestador', text='Emprestador')
        self.emprestimo_table.heading('emprestado_para', text='Emprestado Para')
        self.emprestimo_table.heading('data_emprestimo', text='Data do Empréstimo')

        dados_emprestimo = ler_estoque('emprestimo.txt')

        for i, (item, quantidade, emprestador, emprestado_para, data_emprestimo) in enumerate(dados_emprestimo, start=1):
            self.emprestimo_table.insert(parent='', index='end', iid=i, text=str(i), values=(item, quantidade, emprestador, emprestado_para, data_emprestimo))

        self.emprestimo_table.pack(expand=True, fill='both')
        self.emprestimo_frame.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)
            
    def registra_emprestimo(self):
        data_emprestimo = self.obter_data_atual()
        emprestimo = ItemEmprestimo(self.entry_item.get(),self.entry_qtd.get(),self.entry_nome.get(),self.entry_nome2.get(),data_emprestimo)
        item = Item(self.entry_item.get(),int(self.entry_qtd.get()))
        registrar_emprestimo(emprestimo)
        remover_item(item)
        self.atualizar_tabela_emprestimo()
        self.atualizar_tabela()
        
    def atualizar_tabela_emprestimo(self):
        self.emprestimo_table.delete(*self.emprestimo_table.get_children())

        dados_emprestimo = ler_estoque('emprestimo.txt')

        for i, (item, quantidade, emprestador, emprestado_para, data_emprestimo) in enumerate(dados_emprestimo, start=1):
            self.emprestimo_table.insert(parent='', index='end', iid=i, text=str(i), values=(item, quantidade, emprestador, emprestado_para, data_emprestimo))
        
    def devolver_item(self):
        
        selected_item = self.emprestimo_table.selection()

        if not selected_item:
            messagebox.showerror("Erro", "Nenhum item selecionado.")
            return

        item_id = selected_item[0] 
        item_nome = self.emprestimo_table.item(item_id)['values'][0]  
        item_data = self.emprestimo_table.item(item_id)['values'][4]
        item_emprestador = self.emprestimo_table.item(item_id)['values'][2]  
        item_emprestado_para = self.emprestimo_table.item(item_id)['values'][3] 

        emprestimos = ler_emprestimos()
        
        devolvido = " (devolvido)"
        for emprestimo in emprestimos:
            if emprestimo.nome == item_nome and emprestimo.data_emprestimo == item_data and emprestimo.emprestador == item_emprestador and emprestimo.emprestado_para == item_emprestado_para:
                item = Item(emprestimo.nome,emprestimo.quantidade)
                adicionar_item(item)
                
                emprestimo.nome += devolvido
        
        with open("emprestimo.txt", 'w') as arquivo:
            for emp in emprestimos:
                arquivo.write(f"{emp.nome},{emp.quantidade},{emp.emprestador},{emp.emprestado_para},{emp.data_emprestimo}\n")
                            
        self.atualizar_tabela_emprestimo()
        self.atualizar_tabela()


    def buscar_item(self):
        texto_busca = self.entry_busca.get()
        itens_filtrados = buscar_item(texto_busca)

        for item in self.table.get_children():
            self.table.delete(item)

        for i, (produto, quantidade) in enumerate(itens_filtrados, start=1):
            self.table.insert(parent='', index='end', iid=i, text=str(i), values=(produto, quantidade))
    
    def obter_data_atual(self):
        data_atual = datetime.datetime.now()
        data_formatada = data_atual.strftime("%d/%m/%Y")
        return data_formatada

    

app = Application()
app.mainloop()
