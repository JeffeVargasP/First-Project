from os import system
import math
from utils.utils import getSys

w = ''
l = ''

def calc():
    cont = 0
    volt = continuar = True
    already_gone = False

    while continuar:
        if (volt):
            print('='*80)
            print('''
                [ 1 ] Somar     [ 2 ] Subtrair      [ 3 ] Multiplicar
                [ 4 ] Dividir   [ 5 ] Raiz          [ 6 ] Logaritmo
                [ 7 ] Seno      [ 8 ] Cosseno       [ 9 ] Tangente
                [10 ] Graus     [11 ] Radiano       [12 ] Pi
                                [ s ] Sair
                            ''')
            print('='*80)
            inp = float(input('O que você deseja fazer?: '))
            getSys(w, l)
        if (not(already_gone)):

            if (inp == 1):
                num1 = float(input('Digite o primeiro numero: '))
                num2 = float(input('Digite o segundo numero: '))
                cont = num1 + num2
                getSys(w, l)
                print('O resultado da sua soma é: {}'.format(cont))


            elif (inp == 2):
                num1 = float(input('Digite o primeiro numero: '))
                num2 = float(input('Digite o segundo numero: '))
                cont = num1 - num2
                getSys(w, l)
                print('O resultado da sua subtração é: {}'.format(cont))


            elif (inp == 3):
                num1 = float(input('Digite o primeiro numero: '))
                num2 = float(input('Digite o segundo numero: '))
                cont = num1 * num2
                getSys(w, l)
                print('O resultado da sua multiplicação é: {}'.format(cont))


            elif (inp == 4):
                num1 = float(input('Digite o primeiro numero: '))
                num2 = float(input('Digite o segundo numero: '))
                cont = num1 / num2
                getSys(w, l)
                print('O resultado da sua divisão é: {}'.format(cont))

            elif (inp == 5):
                num1 = float(input('Qual número você quer saber a raiz? '))
                raiz = math.sqrt(num1)
                print(f'A raiz de {num1} é {raiz}')

            elif (inp == 6):
                num1 = float(input('Qual número você quer saber o log? '))
                log10 = math.log10(num1)
                print(f'O log de {num1} da base 10 é {log10}')

            elif (inp == 7):
                num1 = float(input('Qual número você deseja saber o seno? '))
                sen = math.sin(num1)
                print(f'O seno de {num1} é {sen}')

            elif (inp == 8):
                num1 = float(input('Qual número você deseja saber o cosseno? '))
                cos = math.cos(num1)
                print(f'O cosseno de {num1} é {cos}')

            elif (inp == 9):
                num1 = float(input('Qual número você deseja saber a tangente? '))
                tan = math.tan(num1)
                print(f'A tangente de {num1} é {tan}')


            elif (inp == 10):
                num1 = float(input('Qual é a medida em radiano que você quer converter pra grau? '))
                grau = math.degrees(num1)
                print(f'{num1} radianos são equivalentes a {grau} graus')

            elif (inp == 11):
                num1 = float(input('Qual é a medida em graus que você quer converter pra radiano? '))
                radi = math.radians(num1)
                print(f'{num1} graus são equivalentes a {radi} radianos')

            elif (inp == 12):
                num1 = float(input('Qual número você deseja multiplicar por Pi: '))
                pi = math.pi
                picalc = math.pi * num1
                print(f'A constante Pi = {pi} vezes {num1} é igual á {picalc}')

            elif (inp == 's'):
                volt = False
                break

        else:
            if (inp == 1):
                num1 = float(input('Digite o numero: '))
                cont += num1
                getSys(w, l)
                print('O resultado da sua soma é: {}'.format(cont))


            elif (inp == 2):
                num1 = float(input('Digite o numero: '))
                cont -= num1
                getSys(w, l)
                print('O resultado da sua subtração é: {}'.format(cont))


            elif (inp == 3):
                num1 = float(input('Digite o numero: '))
                cont *= num1
                getSys(w, l)
                print('O resultado da sua multiplicação é: {}'.format(cont))


            elif (inp == 4):
                num1 = float(input('Digite o numero: '))
                cont /= num1
                getSys(w, l)
                print('O resultado da sua divisão é: {}'.format(cont))

            elif (inp == 5):
                num1 = float(input('Qual número você quer saber a raiz? '))
                raiz = math.sqrt(num1)
                print(f'A raiz de {num1} é {raiz}')

            elif (inp == 6):
                num1 = float(input('Qual número você quer saber o log? '))
                log10 = math.log10(num1)
                print(f'O log de {num1} da base 10 é {log10}')

            elif (inp == 7):
                num1 = float(input('Qual número você deseja saber o seno? '))
                sen = math.sin(num1)
                print(f'O seno de {num1} é {sen}')

            elif (inp == 8):
                num1 = float(input('Qual número você deseja saber o cosseno? '))
                cos = math.cos(num1)
                print(f'O cosseno de {num1} é {cos}')

            elif (inp == 9):
                num1 = float(input('Qual número você deseja saber a tangente? '))
                tan = math.tan(num1)
                print(f'A tangente de {num1} é {tan}')

            elif (inp == 10):
                num1 = float(input('Qual é a medida em radiano que você quer converter pra grau? '))
                grau = math.degrees(num1)
                print(f'{num1} radianos são equivalentes a {grau} graus')

            elif (inp == 11):
                num1 = float(input('Qual é a medida em graus que você quer converter pra radiano? '))
                radi = math.radians(num1)
                print(f'{num1} graus são equivalentes a {radi} radianos')

            elif (inp == 12):
                num1 = float(input('Qual número você deseja multiplicar por Pi: '))
                pi = math.pi
                picalc = math.pi * num1
                print(f'A constante Pi = {pi} vezes {num1} é igual á {picalc}')

            elif (inp == 's'):
                continuar = False

        already_gone = True
        volt = False
        nex = input('Deseja continuar? [n/s]: ').upper()[0]
        if (nex == 'N'):
            print('='*80)
            print('''
                        [ 1 ] Menu
                        [ 2 ] Limpar
                        [ 3 ] Sair
            ''')
            print('=' * 80)
            choice = int(input('Qual será sua escolha?: '))
            if (choice == 1):
                volt = True
            elif (choice == 2):
                cont = 0
                volt = True
                already_gone = False
            elif (choice == 3):
                continuar = False
        if (nex == 'S'):
            volt = True
        getSys(w, l)
