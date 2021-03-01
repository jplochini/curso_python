#PASSANDO UM NÚMERO ARBITRÁRIO DE ARGUMENTOS

def faz_pizza(*ingredientes):
    """Exibimos os ingredientes da pizza"""
    print("Os ingredientes são: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")

#Mostrando argumentos posicionais e arbitrários

def fazer_pizza(tam, *ingredientes):
    """Exibimos o tamanho e os ingredientes"""
    print(f"Montando a pizza de {tam} pedaços com os ingredientes: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")

#Usando argumentos nomeados arbitrários







