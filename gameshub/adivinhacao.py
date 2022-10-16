from os import system
from random import randint
from time import sleep
from utils.utils import getSys

w = ''
l = ''

def adivinhacao():
    computer = randint(0, 10)
    print('\033[1;31mPENSANDO...')
    sleep(1)
    print('\033[1;33m*-*' * 20)
    print('Estou pensando em um número entre 0 e 10... Você consegue adivinhar?')
    print('\033[1;33m*-*' * 20)
    acertou = False
    tentativas = 0
    while acertou != True:
        print('\033[1;31mPENSANDO...')
        sleep(0.5)
        player = int(input('\033[1;31mEm qual número eu pensei: \033[m'))
        tentativas += 1
        if player == computer:
            print('\033[1;36mAcertou com {} tentativa(s). Parabéns!\033[m'.format(tentativas))
            acertou = True
            print('pressione enter para continuar...')
            input('')
            getSys(w, l)
        elif player < computer:
            print('\033[1;31mMAIOR...\033[33mTente mais uma vez\033[m')
        else:
            print('\033[1;31mMENOR...\033[33mTente novamente.\033[m')
            