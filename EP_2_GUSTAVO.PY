# Iniciando o Jogo de Dominó
def inicia_jogo(jogadores,pecas):

    domino = {'jogadores':{}}
    i = 0

    while i < jogadores:

        domino['jogadores'][i] = pecas[0:7]
        del pecas[0:7]
        
        i += 1
    domino['monte'] = pecas
    domino['mesa'] = []
    
    return domino


# Quem ganhou no dominó?
def verifica_ganhador(ganhador):

    for x,y in ganhador.items():
       
        if y == [] :
            return x
    
    return -1


# Posições possíveis da mão-VERSÃO GUSTAVO
def posicoes_possiveis(mesa,pecas):

    pontas =[]
    possibilidades =[]

    if mesa == []:

        possibilidades = [0,1,2,3,4,5,6]

    if len(mesa) == 1:

        pontas.append(mesa[0][0])
        pontas.append(mesa[0][1])

    elif len(mesa) > 1:

        pontas.append(mesa[0][0])
        pontas.append(mesa[-1][1])

    for a in pecas:

        for b in a:

            if b in pontas:

                if pecas.index(a) not in possibilidades:
                    
                    possibilidades.append(pecas.index(a))

    
    return possibilidades    