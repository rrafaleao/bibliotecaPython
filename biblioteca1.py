class Livro:
    def __init__(self, titulo, isbn, autor):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"{self.titulo} - {self.autor} ({status})"

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livros_emprestados.append(livro)
            print(f"Livro '{livro.titulo}' emprestado.")
        else:
            print(f"Livro '{livro.titulo}' indisponível.")

    def devolver(self, livro):
        if livro in self.livros_emprestados:
            livro.disponivel = True
            self.livros_emprestados.remove(livro)
            print(f"Livro '{livro.titulo}' devolvido.")
        else:
            print("Livro não encontrado entre os emprestados.")

def menu():
    print("\nMenu:")
    print("1. Adicionar Livro")
    print("2. Buscar Livro")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Sair")
    return input("Escolha uma opção: ")

def main():
    biblioteca = []
    usuario = Usuario(input("Nome do usuário: "))

    while True:
        opcao = menu()

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            biblioteca.append(Livro(titulo, autor))
            print("Livro adicionado.")

        if opcao == "2":
            termo = input("Buscar por título ou autor: ").lower()
            encontrados = [livro for livro in biblioteca if termo in livro.titulo.lower() or termo in livro.autor.lower()]
            if encontrados:
                for livro in encontrados:
                    print(livro)
            else:
                print("Nenhum livro encontrado.")

        if opcao == "3":
            termo = input("Título do livro para emprestar: ").lower()
            for livro in biblioteca:
                if termo == livro.titulo.lower():
                    usuario.emprestar(livro)
                    break
            else:
                print("Livro não encontrado.")
        elif opcao == "4":
            termo = input("Título do livro para devolver: ").lower()
            for livro in usuario.livros_emprestados:
                if termo == livro.titulo.lower():
                    usuario.devolver(livro)
                    break
            else:
                print("Você não possui esse livro.")
        if opcao == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
