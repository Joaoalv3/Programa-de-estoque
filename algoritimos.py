class Item:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
class ItemEmprestimo(Item):
    def __init__(self, nome, quantidade, emprestador, emprestado_para, data_emprestimo):
        super().__init__(nome, quantidade)
        self.emprestador = emprestador
        self.emprestado_para = emprestado_para
        self.data_emprestimo = data_emprestimo
    
class Usuario:
    def __init__(self,login,senha,nome):
        self.login = login
        self.senha = senha
        self.nome = nome
    
    def __str__(self):
        return f"Usuario(login={self.login},senha={self.senha,} nome={self.nome})"
    
    def __repr__(self):
        return self.__str__()
        
def ler_usuarios():
    usuarios = []
    try:
        with open("login.txt", 'r') as arquivo:
            for linha in arquivo:
                login, senha ,nome = linha.strip().split(',')
                usuario = Usuario(login, senha, nome)
                usuarios.append(usuario)
    except FileNotFoundError:
        print("erro")
        return []
    return usuarios



def cadastra_usuario(new_user):
    with open("login.txt", "a") as arquivo:
        linha = f"{new_user.login},{new_user.senha},{new_user.nome}\n"
        arquivo.write(linha)

def ler_itens():
    itens = []
    try:
        with open("estoque.txt", 'r') as arquivo:
            for linha in arquivo:
                nome, quantidade = linha.strip().split(',')
                item = Item(nome, int(quantidade))
                itens.append(item)
    except FileNotFoundError:
        return []
    return itens  

def ler_emprestimos():
        emprestimos = []
        try:
            with open("emprestimo.txt", 'r') as arquivo:
                for linha in arquivo:
                    nome, quantidade, emprestador, emprestado_para, data_emprestimo = linha.strip().split(',')
                    emprestimo = ItemEmprestimo(nome, quantidade, emprestador, emprestado_para, data_emprestimo)
                    emprestimos.append(emprestimo)
        except FileNotFoundError:
            print("erro")
            return []
        return emprestimos
    
def ler_estoque(arquivo):
    try:
        with open(arquivo, 'r') as file:
            linhas = file.readlines()
    except FileNotFoundError:
        return []
    return [linha.strip().split(',') for linha in linhas]


def adicionar_item(novo_item):
    itens = ler_itens()
    item_encontrado = False
    for item in itens:
        if item.nome == novo_item.nome:
            item.quantidade = int(novo_item.quantidade) + item.quantidade
            item_encontrado = True
            break

    if not item_encontrado:
        itens.append(novo_item)

    with open("estoque.txt", 'w') as arquivo:
        for item in itens:
            arquivo.write(f"{item.nome},{item.quantidade}\n")


def buscar_item(texto_busca):
    dados = ler_estoque('estoque.txt')
    itens_filtrados = []

    if not texto_busca:
        itens_filtrados = dados
    else:
        for produto, quantidade in dados:
            if texto_busca.lower() in produto.lower():
                itens_filtrados.append((produto, quantidade))

    return itens_filtrados

def registrar_emprestimo(novo_emprestimo):
    with open("emprestimo.txt", "a") as arquivo:
        linha = f"{novo_emprestimo.nome},{novo_emprestimo.quantidade},{novo_emprestimo.emprestador},{novo_emprestimo.emprestado_para},{novo_emprestimo.data_emprestimo}\n"
        arquivo.write(linha)

def autenticar_usuario(new_user):
    usuarios = ler_usuarios()
    for usuario in usuarios:
        if usuario.login == new_user.login:
            if usuario.senha == new_user.senha:
                return True
            else:
                return False
    return False

def remover_item(nome_item):
       

            itens = ler_itens()

            for item in itens:
                if item.nome == nome_item.nome:
                    if nome_item.quantidade <= item.quantidade:
                        item.quantidade -= nome_item.quantidade
                        if item.quantidade == 0:
                            itens.remove(item)
                    else:
                        itens.remove(item)

            with open("estoque.txt", 'w') as arquivo:
                for item in itens:
                    arquivo.write(f"{item.nome},{item.quantidade}\n")