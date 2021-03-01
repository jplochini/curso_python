motos = ['honda', 'yamaha', 'suzuki'] ##Elementos da lista
print (motos)

motos[0] = 'ducati' ##Alteramos o valor do primeiro elemento da lista
print (motos)

##Concatenando elementos no final da lista
motos.append('honda')
print (motos)

##Inserindo elementos em uma lista
otos = ['honda', 'yamaha', 'suzuki'] ##Elementos da lista
otos.insert(0, 'ducati')
print (otos)

##Removendo um item usanod a instrução del
motos = ['honda', 'yamaha', 'suzuki'] ##Elementos da lista
print (motos)

del motos[0]
print (motos)

motos = ['honda', 'yamaha', 'suzuki'] ##Elementos da lista
del motos[1]
print (motos)

##Removendo um item com o método pop()
motos = ['honda', 'yamaha', 'suzuki'] ##Elementos da lista
print (motos)
popped_motos = motos.pop()
print (motos)
print (popped_motos)
print ("A ultima moto que compramos foi uma " + popped_motos.title() + ".")

##Removendo itens de qualquer posição em uma lista
motos = ['honda', 'yamaha', 'suzuki']
first_compra = motos.pop(0)
print ("A primeiro moto nossa foi uma " + first_compra.title() + ".")

##Removendo um item de acordo com o valor
motos = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motos)
motos.remove('honda')
print (motos)

too_expansive = 'ducati'
motos.remove(too_expansive)
print (motos)
print ("\nA " + too_expansive.title() + " is a too expensive for me.")

##Faça voce mesmo:
print ('Faca voce mesmo:\nEXERCICIOS: ')
print ("3.4- Lista de convidados: ")


conv = ['gabi', 'duda', 'debora'] ##Lista de convidados
print ('Ola ' + conv[0].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[1].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[2].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado

print ('\n3.5- Alterando a lista de convidados: ')


conv = ['gabi', 'duda', 'debora'] ##Lista de convidados
print ('O convidado ' + conv[2].title() + ' nao podera comparecer a festa :(\n')
conv[2] = 'joao' ##Alterando o nome do convidado na posicao [2]
print ('Ola ' + conv[0].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[1].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[2].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado

print ('\n3.6- Mais convidados:\n ')


conv = ['gabi', 'duda', 'debora'] ##Lista de convidados
conv[2] = 'joao' ##Alterando o nome do convidado na posicao [2]
print ('Ola ' + conv[0].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[1].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[2].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado

print ('\nGostaria de avisar a todos que aluguei uma mesa maior!\n')

conv.insert(0, 'isaac') ##Inserindo o convidado no comeco da lista
conv.insert(2, 'chris') ##Inserindo o convidado no meio da lista
conv.append('maria')  ##Acrescentando um convidado no final da lista

print ('Ola ' + conv[0].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[1].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[2].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[3].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[4].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado
print ('Ola ' + conv[5].title() + ', tudo bem ? Gostaria de convidar voce para minha festa!') ##Mandando a mensagem concatenando ela com o convidado


print ('\n3.7- Reduzindo a lista de convidados: \n')


conv = ['gabi', 'duda', 'debora'] ##Lista de convidados
conv[2] = 'joao' ##Alterando o nome do convidado na posicao [2]
conv.insert(0, 'isaac') ##Inserindo o convidado no comeco da lista
conv.insert(2, 'chris') ##Inserindo o convidado no meio da lista
conv.append('maria')  ##Acrescentando um convidado no final da lista
print (conv)

print ('Infelizmente so chamerei duas pessoas. :(\n') 

ex = conv.pop(0) ##Excluindo o primeiro item da lista 
print (ex)
print ('Voce ficara de fora, ' + ex.title() + '.') 

ex = conv.pop(1) ##Exlucuindo o segundo item da lista
print (ex)
print ('Voce ficara de fora, ' + ex.title() + '.') 

print (conv) ##Verificando as posicoes dos itens

ex = conv.pop(1) ##Excluindo o 'novo' segundo item da lista
print ('Voce ficara de fora, ' + ex.title() + '.')

ex = conv.pop() ##Excluindo o ultimo item da lista
print ('Voce ficara de fora, ' + ex.title() + '.')

print (conv)
del conv[0] ##Excluindo o primeiro item da lista
print (conv)
del conv[0] ##Excluindo o 'novo' primeiro item da lista
print (conv) ##Mostrando a lista vazia

##ORGANIZANDO UMA LISTA

##Ordenando uma lista de forma permanente com o metodo sort()


