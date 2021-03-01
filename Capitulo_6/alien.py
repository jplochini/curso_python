# UM DICIONARIO SIMPLES

alien_0 = {'color': 'green', 'points': 5} #Armazena a cor do alien e sua pontuação

print(alien_0['color'])
print(alien_0['points'])

#TRABALHANDO COM DICIONÁRIOS

alien_0 = {'color': 'green', 'points': 5}

#ACESSANDO VALORES EM UM DICIONÁRIO

print(alien_0['color'])

pontos = alien_0['points']
print(f"You just earned {str(pontos)} points")

#ADICIONANDO NOVOS PARES CHAVE-VALOR

alien_0 = {'color': 'green', 'points': 5}

alien_0['x_position'] = 0
alien_0['y_posotion'] = 25
print( alien_0 )

#COMEÇANDO COM UM DICIONÁRIO VAZIO

alien_0 = {}

alien_0['color'] - 'green'
alien_0['points'] = 5

print( alien_0 )

#MODIFICANDO VALORES EM UMA DICIONÁRIO

alien_0 = {'color': 'green'}
print(f"A cor desse alien é {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"Agora sua cor é : {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"A posição original do alien em x,y é: {str(alien_0['x_position'])}, {str(alien_0['y_position'])}")

#Move o alien pra direita
#Determina a distancia que ele deve se deslocar de acordo com sua velocidade atual

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#A nova posição é a antiga somada ao incremeto
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"A nova posição do alien em x,y é: {alien_0['x_position']}, {alien_0['y_position']}")

#REMOVENDO PARES CHAVE-VALOR

alien_0 = {'color': 'green', 'points': 5}
print( alien_0 )

del alien_0['points']
print( alien_0 )

#UM DICIONÁRIO DE OBJETOS SEMELHANTES

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'js',
    'phil': 'python',
    }

print(f"A linguagem favorita de Jen é {fav_lang['jen'].title()}")

for name, ling in fav_lang.items():
    print(f"{name.title()} e sua linguagem favorira é: {ling.title()}")



#EXERCICIOS

print("Exercicios: ")

#6.1 PESSOA

print("6.1- Pessoa: ")

pessoa = {'nome': 'joão', 'sobrenome': 'lochini', 'idade': 18, 'cidade': 'berlim'}

print("O nome da pessoa é " + pessoa['nome'].title() + " " + pessoa['sobrenome'].title() + 
    ", ele tem " + str(pessoa['idade']) + " anos, e mora em " + pessoa['cidade'].title() + ".")


#6.2 NUMEROS FAVORITOS

print("6.2- Numeros favoritos: ")

num_favs = {'gabi': 10, 'duda': 8, 'jp': 18, 'deh': 50}

print(f"O numero favorito de Gabi é {str(num_favs['gabi'])}")
print(f"O numero favorito de Duda é {str(num_favs['duda'])}")
print(f"O numero favorito de Jp é {str(num_favs['jp'])}")
print(f"O numero favorito de Deh é {str(num_favs['deh'])}")

#6.3 GLOSSÁRIO

print("6.3- Glossário: ")
glos = {'if': 'se', 'for': 'para', 'print': 'mostrar'}

for palavra, significado in glos.items():
    print(f"\nPalavra : {palavra}")
    print(f"Significado: {significado}")

print(f"O significado de if é: {glos['if']}.\n")
print(f"O significado de for é: {glos['for']}.\n")
print(f"O significado de print é: {glos['print']}.\n")

#PERCORRENDO UM DICIONÁRIO COM UM LAÇO

#PERCORRENDO TODOS OS PARES CHAVE-VALOR COM UM LAÇO

user_0 = {
    'user': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }

#UMA LISTA DE DICIONÁRIOS

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#Cria uma lista vazia para armazenar os aliens
aliens = []

#Cria 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#Mostra os 5 primeiros aliens
for alien in aliens[:5]:
    print( alien )
print("...")

#Mostra quantos aliens foram criados
print(f"O numero total de alien criados é: {str(len(aliens))}")

##Cria uma lista vazia para armazenar os aliens
aliens = []

##Cria 30 aliens verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15


#Mostra os 5 primeiros aliens
for alien in aliens[:5]:
    print( alien )

#UMA LISTA EM UM DICIONÁRIO




