##USANDO UM LAÇO WHILE COM LISTAS E DICIONARIOS

#Começa com usuarios que precisam ser verificados,
# e com uma lista vazia para armazenar os usuarios confirmados

nao_confirmados = ['alice', 'brian', 'candace']
confirmados = []

#Verifica cada usuario até que não haja mais usuarios nao verificados,
# Transfere cada usuario verificado para a lista de confirmados

while nao_confirmados:
    current_user = nao_confirmados.pop()

    print (f"Usuario verificado: {current_user.title()}")
    confirmados.append(current_user)

#Exibe todos confirmados
print("\nThe following users have been confirmed: ")
for confirmado in confirmados:
    print(confirmado.title())

#Removendo todas as intâncias de valores específicos de uma lista

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

while 'cat' in pets:
    pets.remove('cat')

print(pets)

#Preenchendo um dicionario com dados de entrada do usuario

responses = {}

#Define uma flag para indicar que a enquete está ativa
polling_active = True

while polling_active:
    #pede o nome e a resposta
    name = input("\nWhat's your name? ")
    response = input("Which mountain would you like to clim someday ? ")
    

    #Armazena a resposta no dicionario
    responses[name] = response

    #descobre se outra pessoa vai responder a enquete
    repeat = input("Would you like to let another person respond ? (yes/no) ")
    if repeat == 'no':
        polling_active = False 

#a enquete foi concluida. Mostra os resultados
print("\n----- Poll results -----")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")

##EXERCICIOS

#7.8 LANCHONETE

print("7.8- Lanchonete: ")

sand_orders = ['atum', 'x-salada', 'calabresa', 'frango', 'x-bacon']
finished_sands = []

while sand_orders:
    current_sands = sand_orders.pop()

    print(f"Preparei seu sanduiche de {current_sands}.")
    finished_sands.append(current_sands)

print("Os sanduiches preparados: ")
for finished_sand in finished_sands:
    print(finished_sand)

#7.9 SEM PASTRAMI

print("7.9- Sem pastrami: ")

sand_orders = ['pastrami', 'atum', 'x-salada', 'pastrami', 'calabresa', 'frango', 'x-bacon', 'pastrami']
finished_sands = []

print("Estamos sem pastrami :( ")

while 'pastrami' in sand_orders:
    sand_orders.remove('pastrami')

print(sand_orders)

while sand_orders:
    current_sands = sand_orders.pop()

    print(f"Preparei seu sanduiche de {current_sands}.")
    finished_sands.append(current_sands)

print("Os sanduiches preparados: ")
for finished_sand in finished_sands:
    print(finished_sand)

#7.10 FERIAS DOS SONHOS

print("7.10- Férias dos sonhos: ")

respostas = {}

flag_ativa = True

while flag_ativa:
    nome = input("Digite aqui seu nome: ")
    resposta = input("Onde você passaria suas férias dos sonhos? ")

    respostas[nome] = resposta

    repete = input("Outra pessoa vai responder ? (yes/no) ")
    if repete == 'no':
        flag_ativa = False
    
print("\n---RESULTADO---")
for nome, resposta in respostas.items():
    print(f"{nome.title()} passaria suas férias em {resposta.title()}.")


