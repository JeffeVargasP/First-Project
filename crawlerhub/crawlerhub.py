from crawlerhub.crawlerImg import crawlerImg
from crawlerhub.dolar import get_dolar
from crawlerhub.euro import get_euro
from crawlerhub.translator import translate
from utils.utils import getSys
from crawlerhub.weather import get_weather
w = ''
l = ''

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
                            [ m ] Menu
                            ''')
        print('='*80)
        option = input('Sua resposta: ')
        getSys(w, l)
        if option == '1':
            city = input('Digite a cidade: ')
            get_weather(city)
        elif option == '2':
            crawlerImg()
        elif option == '3':
            get_euro()
        elif option == '4':
            get_dolar()
        elif option == '5':
            translate()
        elif option == 'm':
            break