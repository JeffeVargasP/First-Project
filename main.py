import sys, time
from crawlerhub.crawlerhub import crawlerhub
from gameshub.gameshub import gameshub
from mathhub.mathhub import mathhub
from utils.utils import getSys

w = ''
l = ''
message = '''
\033[1;34mCENTRAL OF FUNCTIONS v3
DEVELOPED BY @JeffeVargasP AND @Dpbm\n
'''

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.02)

while True:

    print('\033[1;m='*80)
    print('''
O que deseja fazer?

[1] - Crawler
[2] - Games
[3] - Matemática
[s] - Sair

    ''')
    print('\033[1;m='*80)
    option = input('Digite a opção desejada: ')
    getSys(w, l)
    if (option == '1'):
        crawlerhub()
    elif (option == '2'):
        gameshub()
    elif (option == '3'):
        mathhub()
    elif (option == 's'):
        print('Saindo...')
        sys.exit()