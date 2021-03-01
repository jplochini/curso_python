#VERIFICANDO A DOFERENÇA

requested_tops = 'mushrooms'

if requested_tops != 'anchovas':
    print("Hold the anchovas!")


#COMPARAÇÕES NÚMERICAS

idade = 18
idade == 18

#TESTANDO VÁRIAS CONDIÇÕES

requested_tops = ['mushrooms','queijo']

if 'mushrooms' in requested_tops:
    print("Adicione mushrooms.")
if 'pepperoni' in requested_tops:
    print("Adicione pepperoni.")
if 'queijo' in requested_tops:
    print("Adicione quiejo.")

print("Sua pizza foi finalizada!")

##EXERCICÍOS

#5.3 CORES ALIENIGENAS

print("5.3- Cores alienigenas #1: ")

alien_color = 'green'
if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos.")

alien_color = 'red'
if alien_color == 'green':
    print("Você acabou de ganhar 5 pontos.")
else:
    print("Você não ganhou 5 pontos.")

#5.4 CORES ALIENIGENAS

print("5.4- Cores alienigenas #2: ")

alien_color = 'green'
if alien_color == 'green':
    print("Você ganhou 5 pontos por acertar o alienigena.")
else:
    print("Você ganhou 10 pontos.")

alien_color = 'yellow'
if alien_color == 'green':
    print("Você ganhou 5 pontos por acertar o alienigena.")
else:
    print("Você ganhou 10 pontos.")

#5.5 CORES ALIENIGENAS

print("5.5- Cores alienigenas #3: ")

alien_color = 'green'
if alien_color == 'green':
    print("Você ganhou 5 pontos por acertar o alienigena.")
elif alien_color == 'yellow':
    print("Você ganhou 10 pontos.")
else:
    print("Você ganhou 15 pontos.")

alien_color = 'yellow'
if alien_color == 'green':
    print("Você ganhou 5 pontos por acertar o alienigena.")
elif alien_color == 'yellow':
    print("Você ganhou 10 pontos.")
else:
    print("Você ganhou 15 pontos.")

alien_color = 'red'
if alien_color == 'green':
    print("Você ganhou 5 pontos por acertar o alienigena.")
elif alien_color == 'yellow':
    print("Você ganhou 10 pontos.")
else:
    print("Você ganhou 15 pontos.")

#5.6 ESTÁGIOS DA VIDA

print("5.6- Estágios da vida: ")

age = 40
if age < 2:
    print("Você é um bebe.")
elif age < 4:
    print("Você é uma criança.")
elif age < 13:
    print ("Você é um(a) garoto(a).")
elif age < 20:
    print("Você é um adolescente.")
elif age < 65:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")


#5.7 FRUTA FAVORITA

print("5.7- Fruta favorita: ")

fruta_fav = ['maçã', 'morango', 'banana']

if 'morango' in fruta_fav:
    print("Você realmente gosta de morangos!")
if 'acerola' in fruta_fav:
    print("Essa fruta não está na lista.")
if 'maçã' in fruta_fav:
    print("Você realmente gosta de maçã!")
if 'laranja' in fruta_fav:
    print("Essa fruta não está na lista.")
if 'banana' in fruta_fav:
    print("Você realmente gosta de banaans!")

#USANDO INTRUÇÕES IF COM LISTAS

##VERIFICANDO ITENS ESPECIAIS

requested_tops = ['cogumelo', 'queijo', 'pepino']

for requested_top in requested_tops:
    print(f"Adicione {requested_top}.")

print("\nSua pizza foi finalizada.")

requested_tops = ['cogumelo', 'queijo', 'pepino']

for requested_top in requested_tops:
    if requested_top == 'pepino': #IF mostra que está sem pepino
        print("Desculpe. Estamos sem pepino :(")
    else:
        print(f"Adicione {requested_top}.")

print("\nSua pizza foi finalizada.")

#VERIFICANDO SE UMA LISTA NÃO ESTÁ VAZIA

requested_tops = []

if requested_tops:
    for requested_top in requested_tops:
        print(f"Adicione {requested_top}.")
    print("\nSua pizza foi finalizada.")
else:
    print("Você realmente quer uma pizza vazia ?")

#USANDO VARIAS LISTAS

avaliable_toppings = ['cebolinha', 'alface', 'tomate'
                      'pepperoni', 'abacaxi', 'queijo']

requested_tops = ['alface', 'batata frita', 'queijo']

for requested_top in requested_tops:
    if requested_top in avaliable_toppings:
        print(f"Adicione {requested_top}.")
    else:
        print(f"Desculpe, não temos {requested_top}.")

print("\nSua pizza foi finalizada!")

#EXERCICIOS

print("Exercicios: ")

#5.8 OLÁ ADMIN

print("5.8- Olá admin: ")

users = ['joao', 'admin', 'pedro', 'gabi', 'maria']

for user in users:
    if user == 'admin':
        print(f"Olá {user.upper()}, gostaria de ver uma relatório de status ?")
    else:
        print(f"Olá {user.title()}, obrigado por fazer login novamente!")

#5.9 SEM USUARIOS

print("5.9- Sem usuários: ")

users = ['joao', 'admin', 'pedro', 'gabi', 'maria']

if users:
    for user in users:
        print(f"Olá {user}, obrigado por fazer login novamente!")
    else:
        print("Precisamos encontar alguns usuários.")

#5.10 VERIFICANDO NOME DE USUARIOS

print("5.10- Verificando nome de usuários: ")

current_users = ['jp', 'gabi', 'pedro']
new_users = ['deh', 'jp', 'duda']

for new_user in new_users:
    if new_user in current_users:
        print(f"O nome {new_user.lower()} já foi usado. Selecione outro.")
    else:
        print(f"O nome {new_user.lower()} está disponivel.")
    
#5.11 NUMEROS ORDINAIS

print("5.11- Números ordinais: ")

nums = list(range(1,11))
for num in nums:
    if num <= 3:
        if num == 1:
            print("1st")
        if num == 2:
            print("2nd")
        if num == 3:
            print("3rd")
    elif num > 3:
        print(f"{num}th")
    else:
        print(f"Não sei como escreve o {num} em inglês :(")


    






