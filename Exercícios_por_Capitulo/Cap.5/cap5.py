#5.3 - CORES ALIENIGENAS PT.1 (Usando if)

#VERSÃO CERTA
alien_color = ['green', 'yellow', 'red']

alien_color = alien_color[0]

if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos!!")

#VERSÃO FALHA
alien_color = ['green', 'yellow', 'red']

alien_color = alien_color[0]

if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos!!")

#5.4 - CORES ALIENIGENAS PT.2 (Usando if-else)

alien_color = ['green', 'yellow', 'red']

alien_color[2]

if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos!!")
else:
    print("Você acabou de ganhar 10 pontos!")

#5.5 - CORES ALIENIGENAS PT.3 (Usando if-elif-else)

alien_color = ['green', 'yellow', 'red']

alien_color = alien_color[0] #Para mudarmos a pontuação basta mudar a posição

if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos!!")
elif alien_color == 'yellow':
    print("Você acabou de ganhar 10 pontos")
else:
    print("Você acabou de ganhar 15 pontos!")

#5.6 - ESTÁGIOS DE VIDA

age = input("Digite sua idade: ")

if int(age) < 2:
    print("Você ainda é um bebê!")
elif int(age) < 4:
    print("Você é uma criança!")
elif int(age) < 13:
    print("Você é um(a) garoto(a)")
elif int(age) < 65:
    print("Você é um(a) adulto(a)")
else:
    print("Você é idoso(a)")

#5.7 - FRUTAS FAVORITAS

fav_fruits = ['morango', 'maçã', 'banana']

fruit = input("Digite o nome de uma fruta: ")

if fruit in fav_fruits:
    print(f"Você realmente gosta de {fruit}.")

#5.8 - OLÁ ADMIN.

nomes = ['joao', 'lochini', 'gabi', 'admin', 'nobre']

for nome in nomes:
    if nome == 'admin':
        print(f"Olá {nome}, gostaria de ver um relatório de status ?")
    else:
        print(f"Olá {nome.title()}, obrigado por fazer login novamente!")

#5.9 - SEM USUÁRIOS

names = []

if names == []:
    print("A lista está vazia! Precisamos encontrar alguns usuarios")

#5.10 - VERIFICANDO NOMES DE USUÁRIOS

current_users = ['debora', 'maria', 'duda', 'joao', 'paulo']
new_users = ['giovana', 'nobre', 'gabriela', 'joao', 'paulo']

for user in new_users:
    if user in current_users:
        print(f"O nome {user.title()} já esta em uso! escolha outro")



