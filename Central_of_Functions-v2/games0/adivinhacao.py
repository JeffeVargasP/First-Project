from os import system
from random import randint
from time import sleep

def adivinhacao():
    computador = randint(0, 10)
    print('\033[1;31mPENSANDO...')
    sleep(1)
    print('\033[1;33m*-*' * 20)
    print('Estou pensando em um número entre 0 e 10... Você consegue adivinhar?')
    print('\033[1;33m*-*' * 20)
    acertou = False
    tentativas = 0
    while not acertou:
        print('\033[1;31mPENSANDO...')
        sleep(0.5)
        jogador = int(input('\033[1;31mEm qual número eu pensei: \033[m'))
        tentativas += 1
        if jogador == computador:
            acertou = True
        elif jogador < computador:
            print('\033[1;31mMAIOR...\033[33mTente mais uma vez\033[m')
        else:
            print('\033[1;31mMENOR...\033[33mTente novamente.\033[m')
            print('\033[1;36mAcertou com {} tentativas. Parabéns!\033[m'.format(tentativas))
            print('''
            [ 1 ] Sair
            ''')
            choice = str(input('Digite 1 e pressione Enter... '))
            if choice == '1':
                system('cls')
                break
