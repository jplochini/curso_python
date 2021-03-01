##INTRODUÇÃO AOS LAÇOS WHILE

#LAÇO WHILE EM AÇÃO

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

##DEIXANDO O USUARIO DECIDIR QUANDO QUER SAIR

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

message = " "
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

##USANDO UMA FLAG

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("Você saiu do programa!")
    else:
        print(message)

##USANDO BREAK PARA SAIR DE UM LAÇO

prompt = "\nPlease enter the name of city you have visited: "
prompt += "\n(Enter 'quit' to end the program). "

while True:
    city = input( prompt )

    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}! ")

##USANDO CONTINUE EM UM LAÇO

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print( current_number )

##EVITANDO LOOPS INFINITOS

x = 1
while x <= 5:
    print(x)
    x += 1 #Se tirarmos essa linha o laço executa infinitamente


#EXERCICIOS

#7.4 INGREDIENTES PARA UMA PIZZA

print("7.4- Ingredientes para uma pizza: ")

frase = "\nDigite o ingrediente desejado: "


while True:
    mensagem = input( frase )

    if mensagem == 'sair':
        print("Você saiu da seção de ingredientes.")
        break
    else:
        print(f"Você acrescentou {mensagem.title()} !")

#7.5 INGRESSOS PARA O CINEMA

print("7.5- Ingressos para o cinema: ")

idade = ("\nDigite sua idade: ")

while True:
    ver = input(idade)
    
    if int(ver) < 3:
        print ("O ingresso é gratuito.")
    elif int(ver) < 12:
        print ("O ingresso custa 10 doláres.")
    else:
        print ("O ingresso custa 15 doláres.")


#7.6 TRÊS SAÍDAS

print("7.6- Três saídas: ")

#Usanod break
frase = "\nDigite o ingrediente desejado: "


while True:
    mensagem = input( frase )

    if mensagem == 'sair':
        print("Você saiu da seção de ingredientes.")
        break
    else:
        print(f"Você acrescentou {mensagem.title()} !")

#Usando active = True
frase = "\nDigite o ingrediente desejado: "

active = True
while active:
    mensagem = input( frase )

    if mensagem == 'sair':
        print("Você saiu da seção de ingredientes.")
        active = False
    else:
        print(f"Você acrescentou {mensagem.title()} !")

##USANDO UM LAÇO WHILE COM LISTAS E DICIONARIOS





