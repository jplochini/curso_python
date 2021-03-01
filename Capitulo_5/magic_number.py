#COMPARAÇÕES NÚMERICAS

answer = 17

if answer != 42:
    print("Essa não é a idade certa. Tente novamente!")

#USANDO and E or PARA TESTAR VÁRIAS CONDIÇÕES

age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >= 21 #and é usado para fazer duas comparações ao mesmo tempo

age_1 = 22
age_0 >= 21 and age_1 >=21 #Como age_0 e age_1 são maiores que 22 o resultado será verdadeiro

(age_0 >= 21) and (age_1 >= 21) #Podemos usar os () para melhorar a leitura

#USANDO or PARA TESTAR VÁRIAS CONDIÇÕES

idade_0 = 22
idade_1 = 18

(idade_0 >= 21) or (idade_1 >=21) #É verdadeiro pq um dos dois satisfaz a condição

idade_0 = 18

(idade_0 >= 21) or (idade_1 >=21) #É falso pois nenhum satisfaz a condição

#VERFICANDO SE UM VALOR ESTÁ EM UMA LISTA

ingredientes = ['alface', 'cebola', 'calabresa', 'molho']
'molho' in ingredientes #Usamos 'in' para verificar se o ingrediente está na lista de ingredientes

'queijo' in ingredientes #Usamos 'in' para verificar se o ingrediente está na lista de ingredientes

#VERIFICANDO SE UM VALOR NÃO ESTÁ NA LISTA







