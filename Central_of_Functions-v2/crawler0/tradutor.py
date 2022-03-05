from deep_translator import GoogleTranslator
from os import system

def traduzir():
    volt = True
    langs_dict = GoogleTranslator.get_supported_languages(as_dict=True)

    lingua1 = ''
    lingua2 = ''

    while volt:
        while lingua1 not in langs_dict.keys() and lingua2 not in langs_dict.keys() :
            print('='*80)
            lingua1 = input('Língua materna: ')
            lingua1 = (GoogleTranslator(source='pt', target='en').translate(lingua1)).lower()
            lingua2 = input('Língua da tradução: ')
            lingua2 = (GoogleTranslator(source='pt', target='en').translate(lingua2) ).lower()
            pl = input('Digite o texto a ser traduzido: ')


            if not lingua1 in langs_dict.keys():
                print('essa lingua nao existe em nosso sistema {}'.format(lingua1))

            if not lingua2 in langs_dict.keys():
                print('essa lingua nao existe em nosso sistema {}'.format(lingua2))

            if  lingua1 in langs_dict.keys() and lingua2 in langs_dict.keys():
                sigla1 = langs_dict[lingua1]
                sigla2 = langs_dict[lingua2]
                translated = GoogleTranslator(source=sigla1, target=sigla2).translate(pl)
                print(f'A tradução de {pl} é {translated}')
        print('Deseja continuar?')
        print('='*80)
        print('''
                        [ c ] Continuar...
                        [ m ] Menu de Crawler
        ''')
        print('='*80)
        choice = str(input('O que vai ser? '))
        if choice == 'c':
            volt = True
            lingua1 = lingua2 = ''
        if choice == 'm':
            system('cls')
            volt = False
