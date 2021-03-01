#DEFINIDO UMA FUNÇÃO

def greet_user():
    """Exibe uma saudação"""
    print("Hello!!")

greet_user()

#PASSANDO INFORMAÇÕES PARA UMA FUNÇÃO

def greet_user(username):
    """Exibe uma saudação"""
    print(f"Hello {username.title()}!!")

greet_user('Gabriela')

#ARGUMENTOS E PARÂMETROS

#EXERCICIOS

#8.1 MENSAGEM
print("8.1- Mensagem: ")

def display_message():
    """Mostrando oq estou aprendendo"""
    print("Estou aprendendo o que é uma função e para que serve!!")

display_message()

def fav_book(livro):
    """Mostrando o livro favorito"""
    print(f"O meu livro favorito é {livro.title()}!")

fav_book('curso intensivo de python')



