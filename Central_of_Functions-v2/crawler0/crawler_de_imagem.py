import os, sys, time
from os import system
from simple_image_download import simple_image_download as simp
def baixarimagem():
    response = simp.simple_image_download
    print('='*80)
    txt = str(input('Digite o que deseja baixar imagem: '))
    qnt = int(input('Digite a quantidade: '))
    message = 'Processando...'
    response().download(txt, qnt)
    print('Download concluido com sucesso!')
    print('='*80)
    print('''
    [ 1 ] Sair
    ''')
    choice = str(input('Digite 1 e pressione Enter... '))
    if choice == '1':
        system('cls')
