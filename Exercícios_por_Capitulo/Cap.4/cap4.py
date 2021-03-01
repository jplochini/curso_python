#4.1 - PIZZAS

pizzas = ['catufrango', 'calabresa', '4 queijos']

for pizza in pizzas:
    print(f"Gosto de pizza de {pizza.title()}")
print("Eu realmente gosto de pizza!")

#4.2 - ANIMAIS

animais = ['cachorro', 'gato', 'cavalo']

for animal in animais:
    print(f"Um {animal} seria um ótimo animal de estimação.")
print("Qualquer animal desse seria um bom companheiro! :)")

#4.3 - CONTANDO ATÉ VINTE

nums = list(range(1, 21)) #Fazendo uma lista de números de 1 - 20 incluindo-os
print(nums)

#4.4 - UM MILHÃO

millions = list(range(1, 1000001))
for million in millions:
    print(million)

#4.5 - SOMANDO UM MILHÃO

somas = list(range(1, 1000001))
min (somas)
max (somas)
sum (somas)

#4.6 - NÚMEROS ÍMPARES

impares = list(range(1, 21, 2))
for impar in impares:
    print(impar)

#4.7 - TRÊS

tres = list(range(3, 31, 3))
for mult in tres:
    print(mult)

#4.8 - CUBOS

cubos = list(range(1, 11))
for cubo in cubos:
    print(f"{cubo**3}")


#4.9 - COMPREHENSION DE CUBOS

cubos = [valor**3 for valor in range(1, 11)]
print(cubos)

#4.10 - FATIAS

impares = list(range(1, 21, 2))
for impar in impares:
    print(impar)

print("Os três primeiros itens da lista são:")
print(impares[0:3])

print("Os três itens do meio da lista são:")
print(impares[3:6])

print("Os três últimos itens da lista são:")
print(impares[7:10])

#4.11 - MINHAS PIZZAS, SUAS PIZZAS

pizzas = ['catufrango', 'calabresa', '4 queijos']

friend_pizza = ['catufrango', 'calabresa', '4 queijos']

pizzas.append('portuguesa')
friend_pizza.append('brócolis')
for pizza in pizzas:
    print(f"Minhas pizzas favoritas são {pizza.title()}.")

for pizza in friend_pizza:
    print(f"As pizzas favoritas do meu amigo {pizza.title()}.")


