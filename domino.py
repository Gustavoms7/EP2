import Funcoes 

print("Insper Dominó")
print('=-'*70)
print('Bem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores.')
print('Vamos começar!!!')
 

#  perguntar quantos jogadores 

numero_jogadores = int(input('Quantas pessoas vão jogar ?'))

while numero_jogadores <= 1 and numero_jogadores >= 5 :
    print('Número inválido!')

    numero_jogadores = int(input('Quantas pessoas vão jogar ?'))
#embaralhando
pecas=Funcoes.cria_pecas()
#distribuindo
Funcoes.inicia_jogo(numero_jogadores,pecas)




