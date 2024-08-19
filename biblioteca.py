class Livro:
    def __init__(self, titulo, autor, isbn, status):
        self.titulo = titulo
        self.autor = autor 
        self.isbn = isbn
        self.status = status

class Autor:
    def __init__(self, autor, nacionalide):
        self.autor = autor
        self.nacionalide = nacionalide

class Usuario:
    def __init__(self, usuario, id):
        self.usuario = usuario
        self.id = id

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, titulo, autor, isbn, status):
        novo_livro = Livro(titulo, autor, isbn, status)
        self.livros.append(novo_livro)
        print("Livro adicionado à biblioteca.")
    
    def buscar_livro(self, titulo_busca):
        resultados = [livro for livro in self.livros if titulo_busca.lower() in livro.titulo.lower()]
        if resultados:
            print("Livros encontrados:")
            for livro in resultados:
                print(f"{livro.titulo} - {livro.autor} - {livro.status}") 
        else:
            print("Livro não encontrado")
    
    def adicionar_usuario(self, usuario, id):
        novo_usuario = Usuario(usuario, id)
        self.usuarios.append(novo_usuario)
        print(f"Usuário {usuario} adicionado à biblioteca.")

    def empresta_livro(self, titulo_empresta):
        resultados = [livro for livro in self.livros if titulo_empresta.lower() in livro.titulo.lower()]
        if resultados:
            for livro in resultados:
                if livro.status == "Disponivel":
                    livro.status = "Emprestado"
                    print(f"Livro {livro.titulo} emprestado.")
                    return
            print("Nenhum livro disponível para empréstimo.")
        else:
            print("Livro não encontrado.")

    def devolver_livro(self, titulo_devolve):
        resultados = [livro for livro in self.livros if titulo_devolve.lower() in livro.titulo.lower()]
        if resultados:
            for livro in resultados:
                if livro.status == "Emprestado":
                    livro.status = "Disponivel"
                    print(f"Livro {livro.titulo} devolvido.")
                    return
            print("Nenhum livro estava emprestado.")
        else:
            print("Livro não encontrado.")

def menu():
    biblioteca = Biblioteca()
    while True:
        print("<Menu>")
        print("1. Adicionar Livro.")
        print("2. Buscar Livro")
        print("3. Adicionar usuario")
        print("4. Emprestar")
        print("5. Devolver")
        print("6. Sair")
        op = input("Digite a opção: ")

        if op == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            nacionalide = input("Digite a nacionalidade do autor: ")
            isbn = input("Digite o isbn do livro: ")
            status = "Disponivel"
            biblioteca.adicionar_livro(titulo, autor, isbn, status)

        elif op == '2':
            titulo_busca = input("Digite o título do livro para buscar: ")
            biblioteca.buscar_livro(titulo_busca)

        elif op == '3':
            usuario = input("Digite o nome do usuario: ")
            id = input("Digite o id do usuario: ")
            biblioteca.adicionar_usuario(usuario, id)

        elif op == '4':
            titulo_empresta = input("Digite o titulo do livro que deseja emprestar: ")
            biblioteca.empresta_livro(titulo_empresta)

        elif op == '5':
            titulo_devolve = input("Digite o titulo do livro para devolver: ")
            biblioteca.devolver_livro(titulo_devolve)

        elif op == '6':
            print("Você escolheu sair!")
            break

menu()
