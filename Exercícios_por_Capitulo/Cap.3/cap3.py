#3.1 Nomes

names = ['joao', 'gabi', 'nobre', 'joaozinho']

for name in names:
    print( name.title() )

#3.2 Saudações

names = ['joao', 'gabi', 'nobre', 'joaozinho']

for name in names:
    print(f"Olá eu me chamo {name.title()}, prazer em conhecer!")

#3.3 Sua própria lista

motos = ['honda', 'suzuki', 'bmw', 'biz']

for moto in motos:
    print(f"Eu gostaria de ter {moto.title()}.")


#3.4 Lista de convidados

convidados = ['gabriela', 'joão', 'pedro', 'maria']

for convidado in convidados:
    print(f"Olá {convidado.title()}, você está convidado para o jantar!")

#3.5 Alterando a lista de convidados

convidados = ['gabriela', 'joão', 'pedro', 'maria']

for convidado in convidados:
    print(f"Olá {convidado.title()}, você está convidado para o jantar!")

print(f"{convidados[2].title()} você não poderá ir ao jantar!\n")

convidados[2] = 'dudão'

for convidado in convidados:
    print(f"{convidado.title()}, você está convidado!")


#3.6 Mais convidados

convidados = ['gabriela', 'joão', 'pedro', 'maria']

for convidado in convidados:
    print(f"Olá {convidado.title()}, você está convidado para o jantar!\n")

print("Encontrei uma mesa maior para a festa!\n")

convidados.insert(0, 'nobre')
convidados.insert(1, 'lochini')
convidados.append('verginio')

for convidado in convidados:
    print(f"{convidado.title()}, você está convidado!")

#3.7 Reduzindo a lista de convidados

convidados = ['gabriela', 'joão', 'pedro', 'maria']

for convidado in convidados:
    print(f"Olá {convidado.title()}, você está convidado para o jantar!\n")

print("Encontrei uma mesa maior para a festa!\n")

convidados.insert(0, 'nobre')
convidados.insert(1, 'lochini')
convidados.append('verginio')

for convidado in convidados:
    print(f"{convidado.title()}, você está convidado!")

print("\nInfelizmente só poderei convidar duas pessoas :(\n")

fora = convidados.pop(6)
print(f"{fora.title()}, voce não poderá ir :(")
fora2 = convidados.pop(5)
print(f"{fora2.title()}, voce não poderá ir :(")
fora3 = convidados.pop(4)
print(f"{fora3.title()}, voce não poderá ir :(")
fora4 = convidados.pop(3)
print(f"{fora4.title()}, voce não poderá ir :(")
fora5 = convidados.pop(2)
print(f"{fora5.title()}, voce não poderá ir :(")

print(convidados)

for convidado in convidados:
    print(f"{convidado.title()}, você poderá ir :)")

del convidados[1]
del convidados[0]

print(convidados)

#3.8 Conhecendo o mundo

lugares = ['berlim', 'nova york', 'disney', 'japão', 'coreia do sul']

print(lugares)

print(sorted(lugares))

print(lugares)

lugares.reverse()
print(lugares)

lugares.reverse()
print(lugares)

lugares.sort()
print(lugares)

lugares.sort()
print(lugares)









