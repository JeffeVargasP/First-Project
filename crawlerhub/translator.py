from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from utils.utils import getSys
from deep_translator import GoogleTranslator

w = ''
l = ''

def translate():
    langList = GoogleTranslator().get_supported_languages(as_dict=True)
    langList = list(langList.keys())
    print('''
Qual o idioma que você deseja traduzir?
    ''')
    for i in range(len(langList)):
        print(f'[{i}] {langList[i]}')
    lang = input('Sua resposta: ')
    lang = langList[int(lang)]
    print('''
Qual o idioma que você deseja traduzir para?
    ''')
    for i in range(len(langList)):
        print(f'[{i}] {langList[i]}')
    lang2 = input('Sua resposta: ')
    lang2 = langList[int(lang2)]
    text = input('Digite o texto que você deseja traduzir: ')
    translated = GoogleTranslator(source=lang, target=lang2).translate(text)
    print(f'O texto traduzido é: {translated}')
    print('Pressione enter para continuar...')
    input('')
    getSys(w, l)
    return translated