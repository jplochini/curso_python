#UM DICIONÁRIO EM UM DICIONÁRIO

users = {
    'ainstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
}
    
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

#EXERCICIOS

print("Exercicios: ")

#6.7 PESSOAS

print("6.7- Pessoas: ")
    

pessoa0 = {'nome': 'joão', 'sobrenome': 'lochini', 'idade': 18, 'cidade': 'berlim'}
pessoa1 = {'nome': 'gabi', 'sobrenome': 'nobre', 'idade': 16, 'cidade': 'berlim'}
pessoa2 = {'nome': 'eros', 'sobrenome': 'lochini', 'idade': 'nan', 'cidade': 'berlim'}

peoples = [pessoa0, pessoa1, pessoa2]

for people in peoples:
    print( people )

#6.8 ANIMAIS DE ESTIMAÇÃO

print("6.8- Animais de estimção: ")

anim0 = {'tipo': 'cachorro', 'nome_do_dono': 'osvaldo'}
anim1 = {'tipo': 'gato', 'nome_do_dono': 'ricardo'}
anim2 = {'tipo': 'coelho', 'nome_do_dono': 'aurora'}

pets = [anim0, anim1, anim2]
print( pets )

#6.9 LUGARES FAVORITOS

print("6.9- Lugares favoritos: ")

fav_places = {'gabi': 'são paulo', 'joão': 'berlim', 'duda': 'usa'}
for name, place in fav_places.items():
    print(f"O lugar favorito de {name.title()} é {place.title()}.")

#6.10 NUMEROS FAVORITOS

print("6.10- Numeros favoritos: ")

num_favs = {
    'gabi': [12, 16],
    'joão': [12, 18],
    'deh': [20, 22],
    'dudao': [15, 25],
    }

for name, nums in num_favs.items():
    print(f"\nO número favorito de {name.title()} é:")
    for num in nums:
        print(f"{str(num)}")

#6.11 CIDADES

print("6.11- Cidades: ")

cities = {
    'berlim': {
        'pais': 'alemanha',
        'population': '3,769 milhoes',
        'fact': 'muito frio',
        },

    'são paulo': {
        'pais': 'brasil',
        'population': '12,33 milhoes',
        'fact': 'muito quente',
        },

    'londres': {
        'pais': 'inglaterra'
        'population': '8,912 milhoes' ,
        'fact': 'não sei',
        },

}

for city, city_info in cities.items():
    print(f"\nCidade: {city.title()}")
    
    info = city_info['pais'].title() + " " + city_info['population']
    fato = city_info['fact']

    print(f"\tInformações da cidade: {info}")
    print(f"\tFato curioso: {fato}")







