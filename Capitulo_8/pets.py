def describe_pet(animal_type, pet_name):
    """Exibe informações sobre um animal"""
    print(f"Eu tenho um {animal_type}.")
    print(f"O nome do meu {animal_type} é {pet_name}!")

describe_pet('hamster', 'Larry')

#ARGUMNETOS NOMEADOS

def descreve_pet(animal_type, pet_name):
    """Exibe informações sobre pets"""
    print(f"Eu tenho um {animal_type}.")
    print(f"O meu {animal_type} se chama {pet_name}!")

descreve_pet(pet_name = 'george', animal_type = 'gato')

#EXERCICIOS

#8.3 CAMISETA
print("8.3- Camiseta: ")

def make_shirt(tamanho, mensagem):
    print(f"O tamanhho da camiseta é '{tamanho}'.")
    print(f"A mensagem da camiseta é '{mensagem}'.")

make_shirt('M', 'Eu faço Estatística!')

make_shirt(mensagem = 'Eu faço Ciência da Computação!', tamanho = 'G')

#8.4 CAMISETAS GRANDES
print("8.4- Camisetas grandes: ")

def make_shirt(mensagem, tamanho = 'grande'):
    print(f"O tamanhho da camiseta é {tamanho}.")
    print(f"A mensagem da camiseta é '{mensagem}'.")

make_shirt ('Eu amo Python')

def make_shirt(tamanho, mensagem = 'Eu amo Python'):
    print(f"O tamanhho da camiseta é '{tamanho}'.")
    print(f"A mensagem da camiseta é '{mensagem}'.")

make_shirt ('M')
make_shirt ('G')

#8.5 CIDADES

def descreve_city(cidade, pais = 'Alemanha'):
    print(f"{cidade.title()} está localizada na {pais.title()}.")

descreve_city ('berlim')
descreve_city ('munique')
descreve_city ('frankfurt')

#VALORES DE RETORNO

def get_formatted_name (first_name, last_name):
    '''Devolve um nome completo de modo elegante'''
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

#DEIXANDO UM ARGUMENTO OPCIONAL

def get_formatted_name(first_name, middle_name, last_name):
    '''Devolve um nome completo de modo elegante'''
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

#Nome do meio opcional

def get_formatted_name(first_name, last_name, middle_name=''):
    '''Devolve um nome completo de modo elegante'''
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('joão', 'lochini', 'pedro')
print(musician)

musician = get_formatted_name('joao', 'lochini')
print(musician)

#DEVOLVENDO UM DICIONARIO







