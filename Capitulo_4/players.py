#Trabalhando com parte de uma lista

players = ["charles", 'marta', 'michael', 'florence', 'eli']
print( players[0:3] ) #O que está ente conchete [] diz para python mostrar do indice 0 até o indice 2

#Percorrendo uma fatia com um laço

players = ["charles", 'marta', 'michael', 'florence', 'eli']

print ("Here are the first three players on my team: ")
for player in players[:3]:
    print (player.title())

#Copiando uma lista

