from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from utils.utils import getSys

w = ''
l = ''

def get_dolar():
    url = 'https://www.google.com/search?q=dolar+hoje'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    dolar = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
    dolar = dolar.replace('Real brasileiro', '')
    print('O valor do dólar hoje é de R$', dolar)
    print('Pressione enter para continuar...')
    input('')
    getSys(w, l)
    return dolar