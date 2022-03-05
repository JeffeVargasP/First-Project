from crawler0.clima import verclima
from crawler0.dolar import verdolar
from crawler0.euro import vereuro
from crawler0.tradutor import traduzir
from crawler0.covid import covid
from crawler0.crawler_de_imagem import baixarimagem
from os import system
def crawlerhub():
    while True:
        print('='*80)
        print('''
                            O que deseja fazer?
                            [ 1 ] Clima
                            [ 2 ] Crawler de Imagem
                            [ 3 ] Euro
                            [ 4 ] Dolar
                            [ 5 ] Tradutor
                            [ 6 ] Covid
                            [ m ] Menu
        ''')
        print('='*80)
        pergunta = str(input('Sua resposta: '))
        system('cls')
        if pergunta == '1':
            verclima()
        elif pergunta == '2':
            baixarimagem()
        elif pergunta == '3':
            vereuro()
        elif pergunta == '4':
            verdolar()
        elif pergunta == '5':
            traduzir()
        elif pergunta == '6':
            covid()
        elif pergunta == 'm':
            break
