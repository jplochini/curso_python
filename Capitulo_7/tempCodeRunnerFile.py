print("7.10- Férias dos sonhos: ")

respostas = {}

flag_ativa = True

while flag_ativa:
    nome = input("Digite aqui seu nome: ")
    resposta = input("Onde você passaria suas férias dos sonhos? ")

    respostas[nome] = resposta

    repete = input("Outra pessoa vai responder ? (yes/no) ")
    if repete == 'no':
        flag_ativa = False
    
print("\n---RESULTADO---")
for nome, resposta in respostas.items():
    print(f"{nome.title()} passaria em {resposta.title()}.")