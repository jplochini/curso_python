#IMPORTANDO UM MÓDULO COMPLETO 
import pizza

pizza.fazer_pizza(13, 'massa')

#IMPORTANDO FUNÇÕES ESPECÍFICAS

#fazemos assim para importar
#from nom_do_modulo import nome_da_função_0, nome_da_função_1...

from pizza import fazer_pizza, faz_pizza

fazer_pizza(12, 'massa')

#Usando a palavra reservadas 'as' para atribuir um alias a uma função

from pizza import fazer_pizza as mp

mp(15, 'massa')


#Usando a palavra reservada 'as' para atribuir um alias a um módulo

import pizza as p

p.faz_pizza('salsicha')


#IMPORTANDO TODAS AS FUNÇÕES DE UM MÓDULO

from pizza import *

fazer_pizza(12, 'massa', 'tomate')




