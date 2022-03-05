from urllib.request import urlopen, Request
from os import system
def verdolar():
    while True:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.11 (KHTML, like Gecko) '
                              'Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        reg_url = "https://www.google.com/search?channel=fs&client=ubuntu&q=dolar+"

        req = Request(url=reg_url, headers=headers)

        content = str(urlopen(req).read())

        find = '<span class="DFlfde SwHCTb" data-precision="2" data-value="'

        position = int(content.index(find) + len(find))

        dolar = content[ position : position + 4]
        system('cls')
        print('='*40)
        print(f'$1 está custando R${dolar}')
        print('='*40)
        real = int(input('Conversor de Real para Dolar: '))
        convert = real / float(dolar)
        print(f'Você digitou R${real}, convertendo isso o valor obtido em dolar é ${convert:.2f}')
        print('''
        [ 1 ] Sair
        ''')
        choice = str(input('Digite 1 e pressione Enter... '))
        if choice == '1':
            system('cls')
            break
