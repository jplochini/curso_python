##ESCREVENDO PROPTS CLAROS

name = input("Qual seu nome ? ")
print(f"Olá eu sou {name}" )

prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += "\nWhat is your firts name? "
name = input(prompt)
print(f"\nHello {name}")

##USANDO int() PARA ACEITAR ENTRADAS NÚMERICAS

age = input("Qual a sua idade ? ")
age = int(age)
age <= 17

