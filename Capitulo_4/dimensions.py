#TUPLAS

dimensios = (200, 50) ##Definindo uma tupla
print(dimensios[0])
print(dimensios[1])

dimensios[0] = 250 ##NÃO SE PODE ALTERAR O VALOR DE UMA TUPLA *********
print(dimensios[0])

dimensios = (200, 50)
for dimensio in dimensios: #Listando os valores da tupla
    print(dimensio)

print("Original dimensions: ")
for dimensio in dimensios:
    print(dimensio)

dimensios = (400, 100) #Unica forma de mudar o valor de uma tupla
print("\nModified dimensions: ")
for dimensio in dimensios:
    print(dimensio)


#4.13 BUFFET

print("4.13- Buffet: ")

coms = ('arroz', 'feijão', 'carne', 'salada', 'batata')
print("O restaurante oferece: ")
for com in coms:
    print(com)

coms[0] = 'ovo' #Tentando mudar o valor de um item da tupla
print(coms)

coms = ('arroz', 'feijão', 'carne', 'salada', 'batata')

print("Cardápio original: ")
for com in coms:
    print(com)


coms = ('arroz', 'feijão', 'frango', 'ovo', 'batata') #Mudando os valores das tupla

print("Outro cárdapio: ")
for com in coms:
    print(com)






