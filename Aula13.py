import time
import math
import datetime
import statistics
# ----------------------- DESAFIO 46 -------------------------- #
print('CONTAGEM REGRESSIVA')
for i in range(10,-1,-1):
    print('{}'.format(i))
    time.sleep(1)

# ----------------------- DESAFIO 47 -------------------------- #
for i in range(2,50,2):
    print('{}'.format(i))

# ----------------------- DESAFIO 48 -------------------------- #
soma = 0
for i in range(1,500,2):
    if(i%3 == 0):
        soma = soma+i
print('{}'.format(soma))

# ----------------------- DESAFIO 49 -------------------------- #
n_49 = int(input('Entre com um numero: '))
for i in range(0,10):
    print('{} x {} = {}'.format(n_49,i,n_49*i))


# ----------------------- DESAFIO 50 -------------------------- #
soma = 0
for i in range(0,6):
    num_50 = int(input('Entre com um numero'))
    if num_50%2 == 0:
        soma = soma+num_50
print('{}'.format(soma))


# ----------------------- DESAFIO 51 -------------------------- #
num_51 = int(input('Entre com o primeiro termo da PA: '))
num_51_2 = int(input('Entre com a razão da PA: '))
for i in range(0,10):
    print('{}'.format(num_51))
    num_51 = num_51+num_51_2

# ----------------------- DESAFIO 52 -------------------------- #
num_52 = int(input('Digite um numero: '))
x = 0
for i in range(1,num_52+1):
    if (num_52/i !=1 and num_52/i !=num_52 and num_52%i == 0):
        x = 1
if x!= 0:
    print('O numero {} não é primo'.format(num_52))
else:
    print('O numero {} é primo'.format(num_52))


# ----------------------- DESAFIO 53 -------------------------- #
frase = input('Entre com uma frase: ')
frase = ''.join(frase.split())
tamanho = len(frase)
metade = math.floor((len(frase))/2)
x = 0
for i in range(0,metade):
    if frase[i] !=  frase[tamanho-1-i]:
        x = 1
if x == 0:
    print('Palindromo')
else:
    print('Não é palindromo')

# ----------------------- DESAFIO 54 -------------------------- #
contador = 0
for i in range(0,7):
    ano = int(input('Entre com o ano de nascimento'))
    ano_atual = datetime.date.today().year
    if ano_atual-ano>=18:
        contador = contador+1
print('{}'.format(contador))


# ----------------------- DESAFIO 55 -------------------------- #
peso = [0,0,0,0,0]
for i in range(0,5):
    peso[i] = float(input('Entre com um peso'))
print('O maior peso é {}kg e o menor é {}kg'.format(max(peso),min(peso)))



# ----------------------- DESAFIO 56 -------------------------- #
idade = [0,0,0,0]
nome = ['a','a','a','a']
sexo = ['a','a','a','a']
idade_homem = 0
cont = 0
for i in range(0,4):
    nome[i] = input('Entre com um nome')
    idade[i] = int(input('Entre com uma idade'))
    sexo[i] = input('Entre com o sexo M ou F')
    if sexo[i] == 'M' and idade[i]>idade_homem:
        homem_mais_velho = nome[i]
        idade_homem = idade[i]
    if sexo[i] == 'F' and idade[i]<20:
        cont = cont + 1
print('A media da idade é {} anos\nO homem mais velho é {}\n{} tem mais que 20 anos'.format(statistics.mean(idade),homem_mais_velho,cont))


