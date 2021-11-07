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
mesa = domino['mesa']
print(f'Mesa: {mesa}')
minhas_pecas = domino['jogadores'][0]
print(f'Minhas peças: {minhas_pecas}')
posicoes_possiveis = Funcoes.posicoes_possiveis(mesa,minhas_pecas)
print(f'Posições Possíveis: {posicoes_possiveis}')
peca = int(input('Escolha a peça: '))
peca_escolhida = minhas_pecas[peca]
print(f'Peça Escolhida: {peca_escolhida}')
adiciona = Funcoes.adiciona_na_mesa(peca_escolhida,mesa)
print(f'Mesa: {adiciona}')
# verificando ganhador
ganhador = Funcoes.verifica_ganhador(domino)
# verifica soma 
lista_soma = []
for pecas_jogador in domino['jogadores'].values():
    soma = Funcoes.soma_pecas(pecas_jogador)
    lista_soma.append(soma)
posicoes_possiveis = Funcoes.posicoes_possiveis(mesa,pecas)


#Posições possíveis da mão
posicoes_possiveis = Funcoes.posicoes_possiveis(mesa,pecas)
#Adicionando peças a mesa num jogo de dominó
for pecas_jogador in domino['jogadores'].values():
    adiciona = Funcoes.adiciona_na_mesa(pecas_jogador,mesa)
