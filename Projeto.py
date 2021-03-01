##Tentando refazer o projeto de ATP em Python

import random
import statistics

casos_diarios = [4975,5327,3258,8825,1232,1111,19030,4135,3392,2788,7502,9347,
                 9765,9921,7073,6156,3408,6235,8555,12244,8338,2013,7649,2891,
                 9638,8657,8350,9395,7780,5107,2610]

mortes_diarias = [213,113,73,365,389,325,386,262,94,46,434,284,407,207,297,75,
                  60,365,267,321,343,302,82,56,341,313,330,324,260,146,59]

total_casos = [172875,178202,181460,190285,191517,192628,211658,215793,219185,
                221973,229475,238822,248587,258508,265581,271737,275145,281380,
                289935,302179,310517,312530,320179,323070,332708,341365,349715,
                359110,366890,371997,374607]


#Menor valor e maior valor de cada lista
print("Mostraremos o menor e maior valor de cada lista: ")

print("O menor valor de casos diários é: ")
print(min( casos_diarios ))
print(max( casos_diarios ))

print("O menor valor de mortes diárias é: ")
print(min( mortes_diarias ))
print(max( mortes_diarias ))

print("O menor valor de total de casos é: ")
print(min ( total_casos ))
print(max( total_casos ))

#Número de casos por dia
print("Aqui mostraremos o número de casos por dia: ")
for casos_diario in casos_diarios:
    print(casos_diario)

print("Mostraremos a quantidade de mortes por dia: ")
for mortes_diaria in mortes_diarias:
    print(mortes_diaria)

print("Por fim mostraremos o número de total de casos por dia: ")
for total_caso in total_casos:
    print(total_caso)

#Média de cada lista
print("A média de casos diários é: ")
m_cd = sum(casos_diarios) / len(casos_diarios)
print(m_cd)

print("A média de mortes diárias é: ")
m_md = sum(mortes_diarias) / len(mortes_diarias)
print(m_md)

print("A média de total de casos é: ")
m_tc = sum(total_casos) / len(total_casos)
print(m_tc)

#Calculando a mediana
print("A mediana de casos diários é: ")
sorted(casos_diarios)
print(statistics.median(casos_diarios))

print("A mediana de mortes diárias é: ")
sorted(mortes_diarias)
print(statistics.median(mortes_diarias))

print("A mediana de total de casos é: ")
sorted(total_casos)
print(statistics.median(total_casos))



