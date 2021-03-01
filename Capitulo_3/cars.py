##Ordenando uma lista de forma permanente com o metodo sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() ##usa-se .sort() pois é um metodo e nao uma função 
print (cars) ##sort() ordena a lista de forma permanente
cars.sort(reverse=True)
print (cars)

##Ordenando uma lista temporariamente com a função sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']

print ("Essa e a lista original:")
print (cars)

print ("\nEssa e a lista com sorted():")
print(sorted(cars))

print ("\nEssa e a lista original novamente: ")
print (cars)

##Exibindo uma lista em ordem inversa
cars = ['bmw', 'audi', 'toyota', 'subaru']
print (cars)

cars.reverse() ##Usa-se .reverse() pois é um atributo
print (cars)

##Descobrindo o tamanho de uma lista
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

##EXERCICIOS
print ("Faca voce mesmo: \n3.8- Conhencendo o mundo: ")
lug = ['sao paulo', 'alemanha', 'eua', 'canada', 'coreia do sul']

print (lug)

lug = ['sao paulo', 'alemanha', 'eua', 'canada', 'coreia do sul']
print(sorted(lug)) ##Mostrando a lista em ordem mas sem muda-la permanentemente
print (lug) ##Mostrando a lista na sua forma original

lug = ['sao paulo', 'alemanha', 'eua', 'canada', 'coreia do sul']
lug.reverse() ##Revertendo a ordem da lista usando o metodo .reverse()
print (lug) ##Mostrando a lista invertida

lug.reverse() ##Revertendo a lista novamente colocando ela na sua forma inicial
print(lug) ##Mostrando a lista

lug = ['sao paulo', 'alemanha', 'eua', 'canada', 'coreia do sul']
lug.sort() ##usa o metodo .sort() para ordenar a lista de forma peermanente
print (lug) ##Lista ordenada

lug.sort(reverse=True) ##Lista ordenada inversamente usando o metodo .sort(reverse=True)
print (lug) 


print ("\n3.9- Convidados para o jantar: ")
conv = ['gabi', 'duda', 'debora']
len (conv)


print ("\n3.10- Todas as funcoes: ")
planos = ['programar', 'facul','trampo', 'casar', 'data science' ]
print (planos)

print(sorted(planos)) ##Usamos a função sorted() para ordenar de forma temporaria nossa lista
print (sorted(planos,reverse=True)) ##Usamos a funcao sorted(reverse=True) para inverteer a nossa lista

planos = ['programar', 'facul','trampo', 'casar', 'data science' ]
planos.reverse() ##Usamos o metodo .reverse() para inverter a lista de forma permanente
print(planos)
planos.reverse()  ##Usamos o metodo .reverse() para colocar a lista na sua forma original
print(planos)

planos = ['programar', 'facul','trampo', 'casar', 'data science' ]
planos.sort() ##Usamos o metodo .sort() para ordenar a lista de forma permanente
print (planos)
planos.sort(reverse=True) ##Ordenando de modo inverso usando o metodo .sort(reverse=True)
print(planos)

##Inserindo e excluindo itens da lista
planos = ['programar', 'facul','trampo', 'casar', 'data science' ]
print (planos)
planos.append('pos') ##Usamos o metodo .append() para acrescentar um item no final da lista
print (planos)

planos.insert(1, 'bike') ##Usamos o metodo .insert() para acrescentar um item novo numa posicao desejada na lista
print (planos)

del planos[1] ##Removendo um item usando del 
print (planos)

planos.remove('pos')
print (planos)


##Evitando erros de indice quando trabalhar com listas
motos = ['honda', 'yamaha', 'suzuki']

del motos[0]
print(motos)

del motos[0]
print(motos)

del motos[0]
print(motos)

del motos[-1]
print (motos)





