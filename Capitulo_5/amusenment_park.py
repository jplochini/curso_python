#SINTAXE IF-ELIF-ELSE

age = 12

if age < 4:
    print("A entrada é gratis.")
elif (age > 4) and (age < 18):
    print("Você paga 5R$.")
else:
    print("Você paga 10R$.")

#Ou podemos fazer assim
if age < 4:
    preco = 0
elif (age > 4) and (age < 18):
    preco = 5
else:
    preco = 10

print(f"Você pagará {str(preco)} reias.")


#USANDO VÁRIOS BLOCOS ELIF

if age < 4:
    print("A entrada é gratis.")
elif (age > 4) and (age < 18):
    print("Você paga 5R$.")
elif age < 65:
    print("Você paga 10R$.")
else:
    print("Você tem desconto de 5R$.")

#OMITINDO O BLOCO ELSE

if age < 4:
    print("A entrada é gratis.")
elif (age > 4) and (age < 18):
    print("Você paga 5R$.")
elif age < 65:
    print("Você paga 10R$.")
elif age >= 65:
    print("Você tem desconto de 5R$.")

#TESTANDO VÁRIAS CONDIÇÕES

