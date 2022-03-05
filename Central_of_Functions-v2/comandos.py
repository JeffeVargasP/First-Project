from os import system
from crawler0.crawlerhub import crawlerhub
from games0.gameshub import gameshub
from math0.mathhub import mathhub
import os, sys, time

message = '''                           \033[1;34mPROJECT OF FUNCTIONS V2.0
                        DEVOLOPED BY JEFFERSON AND ALEXANDRE\n'''
for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.009)

while True:

    print('\033[1;m='*80)
    print('''
                            O que deseja fazer?
                            [ 1 ] Crawler
                            [ 2 ] Games
                            [ 3 ] Matemática
                            [ s ] Sair
    ''')
    print('=\033[1;m'*80)
    pergunta = str(input('Sua resposta: '))
    system('cls')
    if pergunta == '1':
        crawlerhub()
    elif pergunta =='2':
        gameshub()
    elif pergunta == '3':
        mathhub()
    elif pergunta == 's':
        exit()
