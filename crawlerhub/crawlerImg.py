from urllib import response
from simple_image_download import simple_image_download as simp
from utils.utils import getSys
w = ''
l = ''

def crawlerImg():

    while True:
        print('='*80)
        print('''
        O que deseja fazer?
        [ 1 ] Baixar imagem
        [ 2 ] Sair
        ''')
        print('='*80)
        option = input('Sua resposta: ')
        getSys(w, l)
        if option == '1':
            downloadImages()
        elif option == '2':
            break

def downloadImages():

    response = simp.simple_image_download
    
    print('='*80)
    txt = str(input('Digite o que deseja baixar imagem: '))
    qnt = int(input('Digite a quantidade: '))
    message = 'Processando...'
    response().download(txt, qnt)
    print('Download concluido com sucesso!')
    print('='*80)
    print('Pressione enter para continuar...')
    input('')
    getSys(w, l)
    return message
