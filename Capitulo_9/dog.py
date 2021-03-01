#CRIANDO E USANDO UMA CLASSE

class Dog():
    """Tentando criar um cachorro"""
    def __init__(self, name, age):
        """Inicia os atributos name e age"""
        self.name = name
        self.age = age

    def sit(self):
        """Simula o cachorro sentando"""
        print(f"{self.name.title()} está sentando agora!" )

    def roll_over(self):
        """Simula o cachorro rolando"""
        print(f"{self.name.title()} está rolando agora!")

#Criando uma instância a partir de uma classe

my_dog = Dog('williw', 6)
print(f"My dog's name is {my_dog.name.title()}.")
print(f"My dog is {str(my_dog.age)} years old.")

#Chamando métodos

my_dog.sit()
my_dog.roll_over()


#9.1 - RESTAURANTE

class Restaurant():
    """Vamos tentar criar um restaurante"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"O nome do restaurante é: {self.restaurant_name.title()}.")
        print(f"O tipo de comida do restaurante é: {self.cuisine_type}!\n")

    def open_restaurant(self):
        print(f"O {self.restaurant_name.title()} está aberto agora!")

mr = Restaurant('tacchino', 'italiana')
mr.describe_restaurant()
mr.open_restaurant()

#9.2 TRÊS RESTAURANTES

meu_rest = Restaurant('la tavola', 'italiana')
seu_rest = Restaurant('dom arabe', 'arabe')
nosso_rest = Restaurant('dona vovo', 'brasileira')

meu_rest.describe_restaurant()
seu_rest.describe_restaurant()
nosso_rest.describe_restaurant()

#9.3 - USUÁRIOS

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


