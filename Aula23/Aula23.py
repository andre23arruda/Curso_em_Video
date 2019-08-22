#%% Desafio 113
def leiaInt2(texto = 'Digite um numero inteiro: ', showNumber = False):
    while True:
        n = input(texto)
        if n == '':
            n = 0
            print(f'\x1b[6;30;41m O usuario preferiu não informar valor\x1b[0m')
        try:
            int(n)
            if showNumber:
                print(f'\x1b[6;39;44m Voce digitou o numero {n}\x1b[0m')
            return int(n)
        except Exception as erro:
            print(f'\x1b[6;30;41m {erro.__class__}\x1b[0m')
    

def leiaFloat2(texto = 'Digite um numero real: ', showNumber = False):
    while True:
        n = input(texto)
        if n == '':
            n = 0
            print(f'\x1b[6;30;41m O usuario preferiu não informar valor\x1b[0m')
        try:
            float(n)
            if showNumber:
                print(f'\x1b[6;39;44m Voce digitou o numero {n}\x1b[0m')
            return float(n)
        except Exception as erro:
            print(f'\x1b[6;30;41m {erro.__class__}\x1b[0m')

            
n1 = leiaInt2()
n2 = leiaFloat2()
print(f'\nInteiro: {n1} \nReal: {n2}')

#%% Desafio 114
import requests
source = 'http://pudim.com.br'
try:
    r = requests.get(source)
    print(f'\x1b[6;39;42m Deu bom o site pudim\x1b[0m')
except:
    print(f'\x1b[6;39;41m Ih, site pudim deu ruim\x1b[0m')
    
#%% Desafio 115
from sistema import systemFunctions
systemFunctions.menuRegister()

