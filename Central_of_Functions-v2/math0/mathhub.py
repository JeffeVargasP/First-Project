from os import system
from math0.calculadora import calc
from math0.polegada_centimetro import centimeter
def mathhub():
    while True:
        print('='*80)
        print('''
                            O que deseja fazer?
                            [ 1 ] Calculadora
                            [ 2 ] Polegada para Centímetro
                            [ m ] Menu
        ''')
        print('='*80)
        pergunta = str(input('Sua resposta: '))
        system('cls')
        if pergunta == '1':
            calc()
        elif pergunta == '2':
            centimeter()
        elif pergunta == 'm':
            break
