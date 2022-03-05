from deep_translator import GoogleTranslator
from os import system
from urllib.request import urlopen, Request
def covid():
    while True:
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.11 (KHTML, like Gecko) '
                              'Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        pais = str(input('Digite o nome do país: '))
        lingua1 = (GoogleTranslator(source='pt', target='en').translate(pais)).lower().replace(' ', '')

        reg_url = f"https://www.bing.com/covid/local/{lingua1}"
        req = Request(url=reg_url, headers=headers)

        content = str(urlopen(req).read())

        find = '<div class="confirmed">'

        print(reg_url)