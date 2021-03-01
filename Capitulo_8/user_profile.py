#Usando argumentos nomeados arbitrários

def build_profile(first, last, **user_info):
    profile = {} #Cria um dicionário vazio
    profile['first_name'] = first 
    profile['last_name'] = last
    for key, value in user_info.items(): #para cada chave e valor em user_info criamos uma chave e uma valor associado
        profile[key] = value                # criamos uma chave e uma valor associado
    return profile

build_profile('joao', 'pedro', localização='Presidente Prudente',
                 graduação='Estatística') #Testando a função


#8.12 SANDUÍCHES

def sand(*ingredientes):
    """Exibe um resumo do pedido feito"""
    print("Os ingredientes escolhidos são: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


#8.13 PERFIL DO USUÁRIO

def perfil(primeiro, ultimo, **info):
    perfil = {}
    perfil['primeiro_nome'] = primeiro
    perfil['ultimo_nome'] = ultimo
    for chave, valor in info.items():
        perfil[chave] = valor
    return perfil

perfil('joao', 'lochini', faculdade='Ciência da computação', Semestre='quinto')


#8.14 CARROS

def carro(fabricante, modelo, **informacao_adicional):
    sobre = {}
    sobre['fabricante'] = fabricante
    sobre['modelo'] = modelo
    for chave, valor in informacao_adicional.items():
        sobre[chave] = valor
    return sobre

carro('subaru', 'outback', color='blue', tow_package=True)

#ARMAZENDO SUAS FUNÇÕES EM MÓDULOS

#Importando um módulo completo

