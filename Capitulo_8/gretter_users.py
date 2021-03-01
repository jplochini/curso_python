#PASSANDO UMA LISTA PARA UMA FUNÇÃO

def greet_users(names):
    """Exibe uma saudação simples a cada nome na lista"""
    for name in names:
        print(f"Hello {name.title()}!")

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

#MODIFICANDO UMA LISTA EM UMA FUNÇÃO

#***********SEM USAR FUNÇÃO***********
#começa com alguns designs que devem ser impressos
unp_design = ['iphone case', 'robot pendant', 'dobecahedron']
comp_models = []

#Simula a impressão de cada design, até não ter mais nenhum
#Transfere cada design para comp_models após a impressão
while unp_design:
    current_design = unp_design.pop()

    #Simula a criação de uma impressão 3D a partir do design
    print(f"Printing model: {current_design}")
    comp_models.append(current_design)

#Exibe todos os modelos finalizados
print("\nThe following models have been printed: ")
for comp_model in comp_models:
    print(comp_model)

def print_models(unprinted_designs, completed_models):
    """
    Simula a impressão de cada design, até quando não haja mais nenhum.
    Transfere cada design para completed_models após a impressão.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simula a criação de uma impressão 3D a partir do design
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Mostra todos os modelos impressos"""
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


#EVITANDO QUE UMA FUNÇÃO MODIFIQUE UMA LISTA

#EXERCICIOS

#8.9 - MÁGICOS

def show_magicians(nomes):
    for nome in nomes:
        print(nome.title())
    

magos = ['houdini', 'joaodini', 'gabidini']
show_magicians(magos)


#8.10 - GRANDES MÁGICOS

##JEITO CORRETO
def show_magicians(magos, magos_completo):
    while magos:
        magos_atuais = magos.pop()

        print(f"\nMudando o nome do mago: {magos_atuais}")
        magos_completo.append(magos_atuais)

def make_great(magos_completo):
    """Acrescenta o GRANDE no nome do mago"""
    print("\n")
    for mago_completo in magos_completo:
        print(f"O Grande {mago_completo.title()}")


magos = ['houdini', 'joaodini', 'gabidini']
magos_completo = []

show_magicians(magos, magos_completo)
make_great(magos_completo)


#8.11 - MÁGICOS INALTERADOS

def show_magicians(magos, magos_completo):
    while magos:
        magos_atuais = magos.pop()

        print(f"\nMudando o nome do mago: {magos_atuais}")
        magos_completo.append(magos_atuais)

def make_great(magos_completo):
    """Acrescenta o GRANDE no nome do mago"""
    print("\n")
    for mago_completo in magos_completo:
        print(f"O Grande {mago_completo.title()}")

magos = ['houdini', 'joaodini', 'gabidini']
magos_completo = []

show_magicians(magos[:], magos_completo)
make_great(magos_completo)

#PASSANDO UM NÚMERO ARBITRÁRIO DE ARGUMENTOS



