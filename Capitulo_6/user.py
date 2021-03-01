#PERCORRENDO UM DICIONÁRIO COM UM LAÇO

#PERCORRENDO TODOS OS PARES CHAVE-VALOR COM UM LAÇO

user_0 = {
    'user': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
    }

for key, value in user_0.items(): #Modo de usar for em um dicionário
    print(f"\nKey: {key}")
    print(f"Valor: {value}")

#PERCORRENDO TODAS AS CHAVES DE UM DICIONÁRIO COM UMA LAÇO

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'js',
    'phil': 'python',
    }

for name in fav_lang.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in fav_lang.keys():
    print(name.title())

    if name in friends:
        print(f" Hi {name.title()}, eu vi que sua linguagem favorita é {fav_lang[name].title()}")

if 'erin' not in fav_lang.keys():
    print("Erin, dê sua opinião.")

#PERCORRENDO AS CHAVES DE UM DICIONÁRIO EM ORDEM EM UMA LAÇO

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'js',
    'phil': 'python',
    }

for name in sorted(fav_lang.keys()):
    print(f"{name.title()} obrigado por participar!")

#PERCORRENDO TODOS OS VALORES DE UM DICIONÁRIO COM UM LAÇO

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'js',
    'phil': 'python',
    }

print("Vamos ver as linguagens mencionadas: ")
for lang in set(fav_lang.values()): #Usamos set() para evitar os valores repetidos
    print(lang.title())

#EXERCICIOS

print("Exercicios: ")

#6.4 GLOSSARIO 2

print("6.4- Glossário 2: ")

glos = {'if': 'se', 'for': 'para', 'print': 'mostrar'}

for palavra, significado in glos.items():
    print(f"\nPalavra: {palavra}")
    print(f"Significado: {significado}")

glos['key'] = 'chave' #Adicionando um novo par chave-valor no dicionario
glos['value'] = 'valor' #Adicionando um novo par chave-valor no dicionario
glos['title'] = 'titulo' #Adicionando um novo par chave-valor no dicionario

for palavra, significado in glos.items():
    print(f"\nPalavra: {palavra}")
    print(f"Significado: {significado}")

#6.5 RIOS

print("6.5- Rios: ")

rios = {'nilo': 'egito', 'amazonas': 'brasil', 'tigres': 'mediterraneo'}
for rio in rios.keys():
    if rio == 'nilo':
        print("O rio Nilo corre pelo Egito.")
    if rio == 'amazonas':
        print("O rio Amazonas corre pelo Brasil.")
    if rio == 'tigres':
        print("O rio Tigres corre pelo Mediterraneo")

for rio in rios.keys():
    print(f"O rio é: {rio.title()}")

for pais in rios.values():
    print(f"O país é: {pais.title()}")

#6.6 ENQUETES

print("6.6- Enquetes: ")

fav_lang = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'js',
    'phil': 'python',
    }

fav_lang['joao'] = 'R'
fav_lang['gabi'] = 'css'
fav_lang['deh'] = 'html'

pessoas = ['joao', 'gabi', 'edward', 'sarah']

for name in fav_lang.keys():
    

    if name in pessoas:
        print(f"{name.title()}, obrigado por participar!")
    
    if name not in pessoas:
        print(f"{name.title()}, por favor participe da enquete!")

#INFORMAÇÕES ANINHADAS

#UMA LISTA DE DICIONÁRIOS








