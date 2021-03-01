## Capitulo 4 - Trabalhando com listas:


## Percorrendo uma lista inteira com um laço:
magicos = ['alice', 'david', 'carol']
for magico in magicos: ##Se le como "para todo magico na lista de magicos, exiba o nome do magico"
    print(magico)

## Executando mais tarefas com o laço for:
magicos = ['alice', 'david', 'carol']
for magico in magicos:
    print(magico.title() + ", foi um bom truque!") ##Essa mensagem aparecera para todo o magico da listas de magicos
    print ("Eu posso ver seu proximo truque, " + magico.title() + ".\n")

## Fazendo algo apos um laço for
magicos = ['alice', 'david', 'carol']
for magico in magicos:
    print(magico.title() + ", foi um bom truque!") ##Essa mensagem aparecera para todo o magico da listas de magicos
    print ("Eu posso ver seu proximo truque, " + magico.title() + ".\n")

print ( "Obrigado a todos os magicos, foram otimos os truques!" )

## EXERCICIOS

## 4.1- Pizzas:

print ( "4.1 - Pizzas: " )
pizzas = ['calabresa', 'catufrango', 'portuguesa'] # Criando a lista de pizzas
for pizza in pizzas:    # 'para toda pizza da lista, exiba o nome da pizza'
    print ( 'Eu amo pizza de',pizza.title(),'.'  ) # Exibindo a frase para toda a pizza da lista de pizzas

print ( "\nEu gosto de pizza de todos os sabores." ) # Frase nao identada nao entra no laco for


## 4.2 - Animais:

print ( "4.2 - Animais: " )
animais = ['cachorro', 'gato', 'passaro']  # Lista de animais
for animal in animais:      # Para todo animal da lista de animais, exiba o animal
    print ( 'Nao seria nada ruim ter um',animal,'de estimacao!' )   # Exibindo a frase para todo animal da lista de animais

print ( '\nQualqier desses animais seria uma otima escolha!' )    # Frase nao identada nao entra no laco for






