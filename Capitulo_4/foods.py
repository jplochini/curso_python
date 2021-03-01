#Copiando uma lista

my_foods = ['pizza', 'falafel', 'carrot cake']
amigo_food = my_foods[:] #Copiando a lista de 'my_foods' para 'amigo_foods'

my_foods.append ('cannoli') #Acrescentando um novo valor na lista de my_foods
amigo_food.append ('ice cream') #Acrescentando um novo valor na lista de amig_foods

print ("My favorite foods are: ")
print ( my_foods )

print ("\nMy friends favorite foods are: ")
print ( amigo_food )

## EXERCICIOS

#4.10 FATIAS

print ("4.10- Fatias: ")

listas = ['pizza', 'falafel', 'carrot cake']

print("Os três primeiros itens da lista são: ")

for lista in listas[:3]:  #Usando for para listar os itens da lista
    print(lista.title())

print("O item do meio da lista é: ")  
for lista in listas[1:2]:
    print(lista.title())

print("O último item da lista é: ")
for lista in listas[2:3]:
    print(lista.title())


#4.11 MINHAS PIZZAS, SUAS PIZZAS

print("4.11- Minhas pizzas, suas pizzas: ")

pizzas = ['calabresa', 'catufrango', 'portuguesa']
amigo_pizza = pizzas[:]

pizzas.append('4 queijos')
amigo_pizza.append('brocolis')

print("Minhas pizzas favoritas são: ")
for pizza in pizzas[0:5]:
    print(pizza.title())

print("As pizzas favoritas do meu amigo são: ")
for pizza in amigo_pizza[0:5]:
    print(pizza.title())

# TUPLAS




