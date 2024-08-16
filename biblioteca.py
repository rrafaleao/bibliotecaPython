class Livro:
    def __init__(self, titulo, autor, ISBN, disponibilidade):
        self.titulo = input("Digite o titulo do livro: ")
        self.autor = autor 
        self.ISBN = ISBN
        self.disponibilidade = disponibilidade

        def Add_Livro(self):
            Titulo = input("Digite o titulo do livro: ")
            Autor = input("Digite o nome do autor do livro: ")
            Isbn = input("Digite o ISBN do livro: ")
            Disponibilidade = input("Digite a disponibilidade do livro: ")
        
        livro1 = Livro(titulo)


class Autor:
    def __init__(self, nome, nacionalidade):
        nome = nome 
        nacionalidade = nacionalidade

class Usuario:
    def __init__(self, nome, id, livro_emprestado):
        nome = nome
        id = id
        livro_emprestado = livro_emprestado


def main():
    while True:
        print("<Menu>")
        print("1. Adicionar livro")
        print("2. Buscar Livro")
        print("3. Emprestar")
        print("4. Devolver")
        escolha = input("Digite a opção que deseja: ")

        #if escolha == '1':
            #Livro.Add_Livro()

main()

