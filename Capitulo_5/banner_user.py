#VERIFICANDO SE UM VALOR NÃO ESTÁ NA LISTA

banned_users = ['andrew', 'joao', 'gabi']

user = 'maria'

if user not in banned_users: #Usamos 'not' para deixar claro que não está na lista
    print (f"{user.title()} , you can post a response if you wish.")

#EXPRESSÕES BOOLEANAS

game_active = True
can_edit = False


##EXERCÍCIOS

#5.1 TESTES CONDICIONAS

print("5.1- Testes condicionais: ")

prg = 'python' 
print ("O programa == 'python' ? Eu acredito que é verdade.")
print (prg == 'python') #Se a variavel for igual ao valor dado então mostrará que é verdade

print ("\nO programa == 'javascript' ? Eu acredito que é falso.")
print (prg == 'javascript') #Se a variavel não for igual ao valor dado então mostrará que éfalso


nome = 'joão'
sobrenome = 'lochini'
idade = 18

print ("É o João Lochini de 18 anos ? Eu acho que sim.")
print ((nome == 'joão') and (sobrenome == 'lochini') and (idade == 18))
#Se as três variáveis forem iguais aos três valores comparados então aparecerá verdade

print ("\nÉ o João Lochini de 18 anos ? Eu acho que não.")
print ((nome == 'gustavo') and (sobrenome == 'lochini') and (idade == 18))
#Se as três variáveis não forem iguais aos três valores comparados então aparecerá falso


#5.2 MAIS TESTES CONDICIONAIS

print ("5.2- Mais testes condicionais: ")

name = 'gabi'
name2 = 'nobre'
age = 16

print ("É a Gabriela Nobre de 16 anos ? Eu acredito que sim.")
print ((name == 'gabi') and (name2 == 'nobre') and (age == 16 ))

print ("É a Gabriela Nobre de 16 anos ? Eu acho que não.")
print ((name == 'gabi') and (name2 == 'dos santos') and (age == 16 ))

#Usando a função lower()
moto = 'Suzuki'
moto == 'suzuki' #É falso pois a variavel está com letras maiusculas
moto.lower() == 'suzuki' #É verdadeiro pq usamos lower()

num = 34
num2 = 23

(num <= 23) or (num2 > 20)

#Verificando se um item está na lista
numbers = list(range(0,9,2))
number = 6
if number in numbers:
    print(f"O numero {number} está na lista de números.")

number = 5
if number not in numbers:
    print (f"O número {number} não está na lista de números.")

#INSTRUÇÕES IF




