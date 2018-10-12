## ============= DESAFIO 96 ============= ##
def area(l,c):
    print('-'*30)
    print(f'A área do terreno {l}m x {c}m é : {l*c}m²')

print('-'*10 + 'Controle de Terrenos' + '-'*10)
l = float(input('LARGURA: '))
c = float(input('COMPRIMENTO: '))
area(l,c)

## ============= DESAFIO 97 ============= ##
def escreva(*texto):
    for t in texto:
        tamanho = len(t)
        print('-'*tamanho)
        print(t)
        print('-'*tamanho)
    
escreva('André','João')

## ============= DESAFIO 98 ============= ##
from time import sleep
def contador(*parametros):
    aux = 1
    for v in parametros:
        z = v[2]
        limite = v[1]
        if z == 0:
            z = 1
        if v[0] > v[1]:
            z = -abs(v[2])
        print(f'A {aux}ª contagem de {v[0]} até {v[1]} de {abs(z)} em {abs(z)} é:')
        if (limite+z)%z == 0 and v[1] > v[0]:
            limite = limite + 1
        elif (limite+z)%z == 0 and v[0] > v[1]:
            limite = limite - 1    
        for i in range(v[0],limite,z):
            print(i,end = ' ')
            sleep(0.2)
        print(' FIM')
        print('-'*10)
        aux += 1
        
contador((1,10,1),(10,0,-2),(10,25,7))

## ============= DESAFIO 99 ============= ##
from time import sleep
def maior(*parametros):
    for valores in parametros:
        m = valores[0]
        nValores = len(valores)
        print('='*20)
        print('Analisando os valores passados... ')
        for v in valores:
            print(v,end = ' ')
            sleep(0.1)
            if m <= v:
                m = v
        print(f'  Foram informados {nValores} valores ')
        print(f'O maior valor informado foi {m}')

maior((1,2,50,4,5,6),(2,6,80))

## ============= DESAFIO 100 ============= ##
import random
from time import sleep

def sorteia(a,b):
    lista = []
    print('Sorteando 5 valores da lista: ',end = '')    
    for i in range(1,6):
        z = random.randint(a, b)
        lista.append(z)
        print(z,end = ' ')
        sleep(0.2)
    print('PRONTO!')
    somaPar(lista)

def somaPar(lista):
    s = 0
    for v in lista:
        if v%2 == 0:
            s+=v
    print(f'Somando os valores pares de {lista}, temos {s}')

lista = sorteia(1,10)




