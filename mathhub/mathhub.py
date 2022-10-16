from mathhub.calculator import calc
from utils.utils import getSys
from gameshub.adivinhacao import adivinhacao
from gameshub.parouimpar import par_ou_impar

w = ''
l = ''

def mathhub():

    while True:
        print('='*80)
        print('''
            O que deseja fazer?
            [ 1 ] Calculadora
            [ m ] Menu
            ''')
        print('='*80)
        option = input('Sua resposta: ')
        getSys(w, l)
        if option == '1':
            calc()
            par_ou_impar()
        elif option == 'm':
            break