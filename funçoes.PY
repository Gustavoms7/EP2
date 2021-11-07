# Criando peças de dominó
def cria_pecas():
	distribuicao=[]
	for i in range(7):
		for e in range(7):
			if [i,e] not in distribuicao and [e,i] not in distribuicao:
				distribuicao.append([i,e])
	random.shuffle(distribuicao)
	return distribuicao


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
import random


#Soma peças do dominó
def soma_pecas(mao):
    soma=0
    for a in mao:
        for b in a:
            soma+=b
    return soma


#Posições possíveis da mão
def posicoes_possiveis(mesa,pecas):
    all=[0,1,2,3,4,5,6]
    if mesa==[]:
        possibilidades=[0,1,2,3,4,5,6]
    else:
        possibilidades=[]
        for a in pecas:
            for b in a:
                if mesa[0][0]==b or mesa[-1][1]==b:
                    if pecas.index(a) not in possibilidades:
                        possibilidades.append(pecas.index(a))
    return possibilidades


#Adicionando peças a mesa num jogo de dominó
def adiciona_na_mesa(peca,mesa):
    mesa_final=[]
    peca_invertida=[peca[1],peca[0]]
    if mesa==[]:
        mesa_final.append(peca)
    else:
        if peca[1]==mesa[0][0]or peca_invertida[1]==mesa[0][0]:
            if peca[1]==mesa[0][0]:
                mesa_final.append(peca)
            elif peca_invertida[1]==mesa[0][0]:
                mesa_final.append(peca_invertida)
            for a in mesa:
                mesa_final.append(a)
        elif peca[0]==mesa[-1][1] or peca_invertida[0]==mesa[-1][1]:
            for b in mesa:
                mesa_final.append(b)
            if mesa[-1][1]==peca[0]:
                mesa_final.append(peca)
            elif mesa[-1][1]==peca_invertida[0]:
                mesa_final.append(peca_invertida)
    return mesa_final

   