#%% Desafio 57
sexo = 'a'
while sexo != 'M' and sexo!= 'F' :
    sexo = input('Digite o sexo M ou F: ').upper()
print('Sexo correto: {}'.format(sexo))

#%% Desafio 58
from random import *
pc = choice(list(range(0,11)))
jogador = -1
cont = 0
while jogador != pc:
    cont = cont + 1
    jogador = int(input('Entre com um numero:' ))

print('Total de palpites: {}'.format(cont))


#%% Desafio 59
escolha = 4
while escolha !=5:
    if escolha == 1:
        print('[1] SOMA: ')
        print(valor1+valor2)
    elif escolha == 2:
        print('[2] MULTIPLICAÇÃO: ')
        print(valor1*valor2)
    elif escolha == 3:
        print('[3] MAIOR: ')
        if valor1>valor2:
            print('{} > {}'.format(valor1,valor2))
        elif valor1==2:
            print('{} = {}'.format(valor1,valor2))
        else:
            print('{} < {}'.format(valor1,valor2))
    elif escolha == 4:
        print('[4] NOVOS NUMEROS: ')
        valor1,valor2 = int(input('Entre com o primeiro valor:')), int(input('Entre com o segundo valor:'))
    print('------------ Menu ---------------\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5] SAIR')
    escolha = int(input('Escolha uma opção:'))


#%% 60
numero = int(input('Entre com um numero: '))
cont = 1
fat = 1
if numero == 0 or numero == 1:
    print('Fatorial = 1')
else:
    while cont <= numero:
        fat = fat*cont
        cont = cont+1
    print('Fatorial = {}'.format(fat))


#%% Desafio 61 e 62
p1,r = int(input('Primeiro termo: ')),int(input('Razao: '))
cont = 0
pa = p1
print('PA:',end = ' ')
while cont<10:
    print('{}'.format(pa),end = ' ')
    pa = pa+r
    cont = cont+1

usuario = int(input('Deseja ver mais quantos termos? '))
cont = 0
while usuario != 0:
    while cont<usuario:
        print('{}'.format(pa),end = ' ')
        pa = pa+r
        cont = cont+1
    cont = 0
    usuario = int(input('Deseja ver mais quantos termos? '))

print('Encerrado')

#%% Desafio 63
numero = int(input('Entre com um numero: '))
cont = 1
primeiro = 0
segundo = 1
primeiro_aux = 0
print(primeiro, end = ' ')
while cont<numero:
    print(segundo,end = ' ')        
    primeiro_aux = segundo
    segundo = segundo+primeiro
    primeiro = primeiro_aux
    cont = cont + 1
    
#%% Desafio 64
numero = 0
cont = -1
soma = 0
while numero != 999:
    soma = soma+numero
    cont = cont+1
    numero = int(input('Entre com um numero: '))
print(cont,soma)

#%% Desafio 65
numero = int(input('Entre com um numero: '))
maior = numero 
menor = numero
cont = 1
soma = numero
escolha = input('Deseja continuar? [S/n]  ' )
while escolha.upper() == 'S':
    numero = int(input('Entre com um numero: '))
    soma = soma + numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    cont = cont+1
    escolha = input('Deseja continuar? [S/n]  ' )
print('Media: {}\nMaior: {}\nMenor: {}'.format(soma/cont,maior,menor))
