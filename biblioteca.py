class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

class Autor:
    def __init__(self, autor, nacionalidade):
        self.autor = autor
        self.nacionalidade = nacionalidade

class Usuario:
    def __init__(self, nome, id, livros_emprestados):
        self.nome = nome
        self.id = id
        self.livros_emprestados = livros_emprestados

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, titulo, autor, isbn):
        novo_livro = Livro(titulo, autor, isbn)
        self.livros.append(novo_livro)
        print("Livro adicionado à biblioteca.")
    
    def buscar_livro(self, termo):
        resultados = [livro for livro in self.livros if termo.lower() in livro.titulo.lower()]
        if resultados:
            print("Livros encontrados:")
            for livro in resultados:
                status = "disponível" if livro.disponivel else "emprestado"
                print(f" - {livro.titulo} - {livro.autor}")


def menu():
    biblioteca = Biblioteca()
    while True:
        print("<Menu>")
        print("1. Adicionar Livro.")
        print("2. Buscar Livro")
        print("3. Emprestar")
        print("4. Devolver")
        print("5. Sair")
        op = input("Digite a opção: ")

        if op == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o nome do autor: ")
            isbn = input("Digite o isbn do livro: ")
            biblioteca.adicionar_livro(titulo, autor, isbn)          
        elif op == '2':
            termo = input("Digite o título do livro para buscar: ")
            biblioteca.buscar_livro(termo)
        if op == '3':
            pass
        if op == '4':
            pass
        if op == '5':
            print("Você escolheu sair!")
            break

menu()