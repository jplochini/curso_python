class User():
    """Classe contendo informações de usuário"""
    def __init__(self, first_name, last_name, idade):
        self.first_name = first_name
        self.last_name = last_name
        self.idade = idade

    def describe_user(self):
        print("INFORMAÇÕES DO USÁRIO:")
        print(f"Primeiro nome: {self.first_name.title()}")
        print(f"Ultimo nome: {self.last_name.title()}")
        print(f"Idade: {str(self.idade)}")

teste = User('joao', 'lochini', 18)
teste.describe_user()