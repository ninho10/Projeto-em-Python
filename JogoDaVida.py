import os


def ZeroVinte():
    NumVin = 1
    Erro = 0
    while NumVin != 11:
        NumVin = int(
            input('digite o numero que estou pensando, você já errou {} : '.format(Erro)))
        Erro = Erro + 1
    
             
def chefe1():
    RespChe1 = 1

    while RespChe1 != 3:
        RespChe1 = int(input('[1] Vasco   [2] Palmeiras   [3]Flamengo --> '))
        if RespChe1 == 1:
            print('voce errou seu ataque, tente de novo')
        if RespChe1 == 2:
            print('voce acabou de levar um soco assim vai perde, tente de novo')


def jogo(mensagem):
    print('-' * 30)
    print(mensagem)
    print('-' * 30)


print('-' * 50)
print('    ####   SEJA BEM VINDO AO JOGO DA VIDA   ####')
print('-' * 50)
print(' ')
Nome = input(' Jogador Qual è sua Nome? --> ')
AnoNasci = int(input(' Jogador {} que Ano você naisceu? --> '.format(Nome)))
AnoAtual = int(input(' Jogador {} que Ano estamos ?--> '.format(Nome)))

Idade = AnoAtual - AnoNasci
print('Jogador {}, Você tem {} anos ou vai fazer? '.format(Nome, Idade))
N1 = int(input('se você tem, digite [1] se não digite [2] --> '))
print('')
if N1 == 1:
    print('Como pode fazer uma festa e não me chamar, estou triste com Você')
    print('Com isso você perde um vida')
else:
    print('{} estou feliz esse ano tem uma festa para eu ir rsrs. '.format(Nome))
    print('me chamando para festa você ganha uma vida')
print('')
print('')
jogo('    JOGO DA VIDA ')

print('{} vou te fazer um desafio vou pensar em um numero entre 0 e 20 '.format(Nome))
ZeroVinte()
print('Parabéns o numero que eu pensei foi o 11 ')
print('')
os.system('cls')
jogo('    JOGO DA VIDA ')

print('Parabéns jogador {} chegamos no chefe '.format(Nome))
print('vou te fazer uma pergunta acertando você passa de nivel.')

print('Qual é a maior torcida de futbol do Brasil')
chefe1()
print('nossa você atacou o chefe com todo o seu poder........')

print('Parabéns {}, você acabou de derrotar o chefe.......'.format(Nome))
print('#### você passsou para um novo nivel ####')
print('')
