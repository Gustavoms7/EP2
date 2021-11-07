import random
import Funcoes

print("Insper Dominó")
print('=-'*70)
print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
print('Vamos começar!!!')
 

#  perguntar quantos jogadores 
numero_jogadores = int(input('Quantas jogadores ? (2-4)'))

while numero_jogadores <= 1 or numero_jogadores >= 5 :
    print('Número inválido!')

    numero_jogadores = int(input('Quantas pessoas vão jogar ?'))

#embaralhando
pecas=Funcoes.cria_pecas()
#distribuindo
domino = Funcoes.inicia_jogo(numero_jogadores,pecas)
adiciona = domino['mesa']
monte = domino['monte']

i= random.randint(0,numero_jogadores)
while i<=numero_jogadores:
    if i==numero_jogadores:
        i=0
    elif i==0:
        pecas = domino['jogadores'][i]
        print(f'Mesa: {adiciona}')
        print(f'Minhas peças: {pecas}')
        posicoes_possiveis = Funcoes.posicoes_possiveis(adiciona,pecas)
        while True:    
            if posicoes_possiveis==[]:
                print(f'Não possui peças possíveis. Pegando do monte.')
                input('[Pressione Enter]')
                pecas.append(monte[0])
                del monte[0]
                print(pecas)
            else:
                print(f'Posições Possíveis: {posicoes_possiveis}')
                break
        peca = int(input('Escolha a peça: '))
        peca_escolhida = pecas[peca]
        print(f'Peça Escolhida: {peca_escolhida}')
        adiciona = Funcoes.adiciona_na_mesa(peca_escolhida,adiciona)
        del pecas[peca]
        ganhador=Funcoes.verifica_ganhador(domino)
        if ganhador==-1:
            i+=1
        else:
            print(f'Mesa: {adiciona}')
            break
    elif i !=0 :
        pecas = domino['jogadores'][i]
        print(f'Mesa: {adiciona}')
        posicoes_possiveis = Funcoes.posicoes_possiveis(adiciona,pecas)
        while True:    
            if posicoes_possiveis==[]:
                print(f'Não possui peças possíveis. Pegando do monte.')
                pecas.append(monte[0])
                del monte[0]
                print(pecas)
            else:
                break
        peca = random.randint(0,len(posicoes_possiveis)-1)
        peca = posicoes_possiveis[peca]
        peca_escolhida = pecas[peca]
        print(f'Peça Escolhida: {peca_escolhida}')
        adiciona = Funcoes.adiciona_na_mesa(peca_escolhida,adiciona)
        del pecas[peca]
        ganhador=Funcoes.verifica_ganhador(domino)
        if ganhador==-1:
            i+=1
        else:
            print(f'Mesa: {adiciona}')
            break
    




# verificando ganhador
ganhador = Funcoes.verifica_ganhador(domino)
# verifica soma 
lista_soma = []
for pecas_jogador in domino['jogadores'].values():
    soma = Funcoes.soma_pecas(pecas_jogador)
    lista_soma.append(soma)
posicoes_possiveis = Funcoes.posicoes_possiveis(adiciona,pecas)


#Posições possíveis da mão
posicoes_possiveis = Funcoes.posicoes_possiveis(adiciona,pecas)
#Adicionando peças a mesa num jogo de dominó
for pecas_jogador in domino['jogadores'].values():
    adiciona = Funcoes.adiciona_na_mesa(pecas_jogador,adiciona)
