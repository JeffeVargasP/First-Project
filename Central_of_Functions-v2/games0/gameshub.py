from games0.adivinhacao import adivinhacao
from games0.par_ou_impar import par_ou_impar
from os import system
def gameshub():
    while True:
        s = ' Desenvolvido por Jefferson e Alexandre '
        print(s)
        print('='*80)
        print('''
                            O que deseja fazer?
                            [ 1 ] Jogo de Adivinhação
                            [ 2 ] Par ou Ímpar
                            [ m ] Menu
        ''')
        print('='*80)
        pergunta = str(input('Sua resposta: '))
        system('cls')
        if pergunta == '1':
            adivinhacao()
        elif pergunta == '2':
            par_ou_impar()
        elif pergunta == 'm':
            break
