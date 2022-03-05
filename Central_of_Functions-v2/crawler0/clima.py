from os import system
from urllib.request import urlopen, Request
def verclima():
    while True:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.11 (KHTML, like Gecko) '
                              'Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        cidade = str(input('Digite o nome da sua cidade (tudo junto): '))

        reg_url = f"https://www.google.com/search?channel=fs&client=ubuntu&q=clima+{cidade}"
        req = Request(url=reg_url, headers=headers)

        content = str(urlopen(req).read())

        find = '<span class="wob_t TVtOme" id="wob_tm" style="display:inline">'
        find2 = '<span id="wob_pp">'
        find3 = '<span id="wob_hm">'
        find4 = '<span class="wob_t" id="wob_ws">'

        position = int(content.index(find) + len(find))
        position2 = int(content.index(find2) + len(find2))
        position3 = int(content.index(find3) + len(find3))
        position4 = int(content.index(find4) + len(find4))

        clima = content[ position : position + 2]
        precipitation = content[position2 : position2 + 2]
        humidity = content[position3 : position3 + 3]
        wind = content[position4 : position4 + 3]

        print('='*80)
        print(f'''      O clima atual em sua cidade é {clima}ºC
    A precipitação de chuva é de {precipitation}
    A taxa de umidade é de {humidity}
    Os ventos estão à {wind}km/h''')
        print('='*80)
        print('''
        [ 1 ] Sair
        ''')
        choice = str(input('Digite 1 e pressione Enter... '))
        if choice == '1':
            system('cls')
            break
