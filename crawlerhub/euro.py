from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from utils.utils import getSys

w = ''
l = ''

def get_euro():
    url = 'https://www.google.com/search?q=euro+hoje'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    euro = soup.find('div', {'class': 'BNeawe iBp4i AP7Wnd'}).text
    euro = euro.replace('Real brasileiro', '')
    print('O valor do euro hoje é de R$', euro)
    print('Pressione enter para continuar...')
    input('')
    getSys(w, l)
    return euro