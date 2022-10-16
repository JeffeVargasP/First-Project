from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from utils.utils import getSys

w = ''
l = ''

def get_weather(city):
    url = f'https://www.google.com/search?q=clima+em+{city}'
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.get_text().split('°C')[0].split(' ')[-1].lower()
    temp = temp.replace('meteorologia', '')
    temp = temp.replace('clima', '')
    if (temp == ''):
        return 'Cidade não encontrada'
    else:
        print('A temperatura em', city, 'é de', temp, '°C')
        print('Pressione enter para continuar...')
        input('')
        getSys(w, l)
        return temp


