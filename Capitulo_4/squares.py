## Usando range() para criar lista de numeros

squares = []
for valor in range(1,11): # Para todo valor da lista de 1 ate 11
    square = valor**2 # exiba o quadrado do valor
    squares.append(square)

print ( squares )

# Podemos fazer assim tambem
squares = []
for valor in range(1,11): # Para todo valor da lista de 1 ate 11 exiba o quadrado do valor
    squares.append(valor**2)

print ( squares )

# Estatisticas simples com uma lista de numeros

digits = [1,2,3,4,5,6,7,8,9,0]
min ( digits ) # Mostra o menor valor da lista

max ( digits ) # Mostra o maior valor da lista

sum ( digits ) # Soma os valores da lista

# Lista comprehensions

squares = [value**2 for value in range (1,11)]
print ( squares )

##EXERCICIOS

#4.3 CONTANDO ATÉ VINTE

print ("4.3- Contando até vinte: ")

vinte = [value for value in range(0,21)] #Usando lists comprehensions para gerar
                                           #uma sequencia de numeros de 0 até 20
print ( vinte )

#4.4 UM MILHÃO

print ("4.4- Um milhão: ")

milhao = [milho for milho in range (1,1000001)] 
print ( milhao )

#4.5 SOMANDO UM MILHÃO

print ("4.5- Somando um milhão: ")

milhao = [milho for milho in range (1,1000001)]
print ( milhao )

min ( milhao )
max ( milhao )
sum ( milhao )

#4.6 NUMEROS ÍMPARES

print ("4.6- Números ímpares: ")

impar = [im for im in range(1,20,2)] #Gerando uma lista de numeros de 1 até 19,
                                      #sempre somando mais dois a cada número
print ( impar )

#4.7 TRÊS

print ("4.7- Três: ")

tres = [tr for tr in range(3,30,3)] #Gerando uma lista de de números de 3 até 30,
                                      #sempre somando mais 3 a cada número
print ( tres )

#4.8 CUBOS

print ("4.8- Cubos: ")

cubos = [cub**3 for cub in range(1,11)]
print ( cubos )

#4.9 COMPREHENSION DE CUBOS

print ("#4.9 Comprehension de cubos: ")

cubos = [cub**3 for cub in range(1,11)]
print ( cubos )





