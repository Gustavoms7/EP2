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