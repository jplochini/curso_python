name = 'ada lovelace'
print (name.title()) ##Inicia com letra maiuscula
print (name.upper()) ##Todas as letras ficam maiusculas
print (name.lower()) ##Todas as letras ficam minusculas

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print (full_name)
print ("Hello, " + full_name.title() + "!")

mensagem = "Hello, " + full_name.title() + "!"  ##Forma mais simples armazenar a frase em uma variavel
print (mensagem) 

print ("Python")
print ("\tPython")
print ("Languages:\nPython\nC\nJavaScript")
print ("Languages:\n\tPython\n\tC\n\tJavaScript")
##\n serve para ir para a linha de baixo
##\t serve pra dar um espaço

fav_lang = 'python '
print (fav_lang)
print (fav_lang.rstrip()) ##Tira os espaços em branco do lado direito

fav_lang = ' python '
print (fav_lang.rstrip()) ##Remove o espaço em branco do lado direito
print (fav_lang.lstrip()) ##Remove o espaço em branco do lado esquerdo
print (fav_lang.strip()) ##Remove o espaço em branco em ambos os lados
 
