#LISTA EM UM DICIONÁRIO

#Armazena informações sobre a pizza que está sendo pedida

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'cheese'],
    }

#Resumo do pedido

print(f"You ordered a {pizza['crust']}- crust pizza with the follow toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

fav_lang = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['js', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, langs in fav_lang.items():
    print(f"\n{name.title()} sua linguagem favorita é: ")
    for lang in langs:
        print(f"\t{lang.title()}"

#UM DICIONÁRIO EM UM DICIONÁRIO









