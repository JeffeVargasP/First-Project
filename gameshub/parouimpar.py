from utils.utils import getSys
from random import randint
w = ''
l = ''

def par_ou_impar():
    v = 0
    print('\033[1;33m-='*30)
    print('\033[1;32mVAMOS JOGAR UM PAR OU ÍMPAR?')
    print('\033[1;33m-='*30)
    while True:
        valor = int(input('\033[1;34mDigite um valor: '))
        computador = randint(0, 11)
        total = valor + computador
        poi = ' '
        while poi not in 'PI':
            poi = str(input('\033[1;31mPAR \033[1;mou \033[1;33mÍMPAR? [P/I] ')).strip().upper()[0]
        print('\033[1;33m-'*60)
        print('\033[1;34mVocê jogou {} e o computador {}. Total de {}'.format(valor, computador, total), end=' ')
        print('\033[1;31mDEU PAR!' if total % 2 == 0 else '\033[1;33mDEU ÍMPAR!')
        print('\033[1;33m-'*60)
        if poi == 'P':
            if total % 2 == 0:
                print('\033[1;32mVocê venceu!')
                v += 1
            else:
                print('\033[1;31mVocê perdeu!')
        elif poi == 'I':
            if total % 2 == 1:
                print('\033[1;32mVocê venceu!')
                v += 1
            else:
                print('\033[1;31mVocê perdeu!')
        print('\033[1;33m-='*30)
        print('\033[1;31mGAME OVER! \033[1;mVocê \033[1;32mvenceu {} \033[1;mvez(es).'.format(v))
        print('pressione enter para continuar...')
        input('')
        getSys(w, l)
        break
