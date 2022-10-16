from utils.utils import getSys
from gameshub.adivinhacao import adivinhacao
from gameshub.parouimpar import par_ou_impar

w = ''
l = ''

def gameshub():

    while True:
        print('='*80)
        print('''
            O que deseja jogar?
            [ 1 ] Adivinhação
            [ 2 ] Par ou Ímpar
            [ m ] Menu
            ''')
        print('='*80)
        option = input('Sua resposta: ')
        getSys(w, l)
        if option == '1':
            adivinhacao()
        elif option == '2':
            par_ou_impar()
        elif option == 'm':
            break