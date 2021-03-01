#DEVOLVENDO UM DICIONARIO

def build_person(first_name, last_name):
    '''Devolve um dicionário com informações de uma pessoa'''
    person = {'firts': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

#Com um argumento opcional

def build_person(first_name, last_name, age=''):
    '''Devolve um dicionario com informações de uma pessoa'''
    person = {'firts': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

#USANDO UMA FUNÇÃO COM UM LAÇO WHILE

def get_formatted_name (first_name, last_name):
    '''Devolve um nome completo de modo elegante'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

#Este é um loop infinito
while True:
    print("\nPlease tell me your name: ")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

#Fazendo a correção

def get_formatted_name (first_name, last_name):
    '''Devolve um nome completo de modo elegante'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

#Este é um loop infinito
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)") #Nova linha
    f_name = input("First name: ")
    if f_name == 'q': #Nova linha
        break   #Nova linha
    l_name = input("Last name: ")
    if l_name == 'q':   #Nova linha
        break       #Nova linha

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

# EXERCÍCIOS

# 8.6 NOMES DE CIDADE

def city_coutry(cidade, pais):
    local = cidade.title() + ', ' + pais.title()
    return local

morar = city_coutry('berlim', 'alemanha')
print(morar)

# 8.7 ÁLBUM

def make_album(artista, titulo):
    album = {'artista': artista.title(), 'album': titulo.title()}
    return album

art1 = make_album('tim maia', 'sossego')
print(art1)

art2 = make_album('linkin park', 'living things')
print(art2)

def make_album(artista, titulo, faixas=''):
    album = {'artista': artista.title(), 'album': titulo.title()}
    if faixas:
        album['faixas'] = faixas
    return album

art1 = make_album('tim maia', 'sossego', 10)
print(art1)

art2 = make_album('linkin park', 'living things')
print(art2)

# 8.8 ÁLBUNS DOS USUÁRIOS

def make_album(artista, titulo):
    album = {'artista': artista.title(), 'album': titulo.title()}
    return album

while True:
    print("\nPor faavor digite o nome do artista e do álbum: ")
    print("(digite 'q' para sair)")
    a_name = input("Nome do artista: ")
    if a_name == 'q':
        break
    t_name = input("Nome do álbum: ")
    if t_name == 'q':
        break
    

    teste = make_album(a_name, t_name)
    print(teste)


#PASSANDO UMA LISTA PARA FUNÇÃO















