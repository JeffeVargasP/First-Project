from os import system
def centimeter():
    while True:
        c = 2.54
        print('='*80)
        ask = float(input('Digite o valor a ser convertido: '))
        convert0 = float(ask)
        convert1 = convert0 * c
        print(f'Você digitou {convert0} e a conversão resultou em {convert1}cm')
        print('='*80)
        choice = str(input('Digite 1 e pressione Enter... '))
        if choice == '1':
            system('cls')
            break
