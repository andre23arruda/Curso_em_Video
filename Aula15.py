#%% ----------------- DESAFIO 66 ------------------------
soma = 0
cont = 0
while True:
  novo =  int(input('Digite um numero (999 para parar): '))
  if novo == 999:
    break
  soma += novo
  cont += 1   
print(f'A soma dos {cont} valores é {soma}')


#%% ----------------- DESAFIO 67 ------------------------
numero = 0
while True:
  numero = int(input('Deseja ver a tabuada de qual numero?'))
  print('----------------------------------')
  if numero < 0:
    break
  for i in range(0,11):
    print(f'{numero} x {i} = {numero*i}')
  print('----------------------------------')
print('Encerrado')


#%% ----------------- DESAFIO 68 ------------------------
from random import *
print('------------- PAR OU IMPAR -----------')
n_vitorias = 0
while True:
  pc = randint(0,10)
  escolha = input('Par ou impar [P/I]?')
  jogador = int(input('Entre com um numero: '))
  soma = pc+jogador
  print(f'Voce jogou {jogador} e o computador {pc}.\nTotal = {soma}')
  if soma%2 == 0:
    jogo = 'P'
  else:
    jogo = 'I'
  if escolha == jogo:
    n_vitorias += 1
    print(f'Voce VENCEU')
    print('JOGAR NOVAMENTE...')
  else:
    print(f'Voce PERDEU')
    break
print(f'Voce ganhou {n_vitorias} vezes')


#%% ----------------- DESAFIO 69 ------------------------
mulheres20 = 0
homens = 0
adultos = 0
escolha  = '0'

while True:
  sexo = '0'
  escolha  = '0'
  print('---------------- CADASTRO -------------------')
  while sexo != M or sexo != F:
    sexo = input('Digite o sexo da pessoa [M/F] ).upper()
  idade = 'a'
  while not(idade.isnumeric()):
    idade = input('Digite a idade da pessoa: ')
  idade = int(idade)
  if idade > 18:
    adultos += 1
  if sexo == 'M':
    homens += 1
  if sexo == 'F' and idade < 20:
    mulheres20 += 1
  while escolha != 'S' or escolha != N:
    escolha = input('Deseja continuar? [S/N]).upper
  if escolha == 'N':
    breake
                    
print(f'Adultos: {adultos}')
print(f'Homens: {homens}')
print(f'Mulheres abaixo dos 20: {mulheres20}')                    
   
     
#%% ----------------- DESAFIO 70 ------------------------
maisdemil = 0
maisbarato = '0'                    
total = 0
preco0 = 0
cont = 0
print ('--------------- LOJAO DO XXT ---------------')
while True:
  escolha = '0'                    
  nome = input('Nome produto: ')                    
  preco = int(input('Preco do produto R$ '))
  if cont == 0:
      maisbarato = nome
      preco0 = preco
      cont = 1
  else:
      if preco < preco0:
          preco0 = preco
          maisbarato = nome
  if preco > 1000:
      maisdemil += 1
  total += preco   
  while escolha != 'S' and escolha != 'N':
      escolha = input('Deseja continuar? [S/N]').upper()
  if escolha == 'N':
      break
print(f'Total: {total}\nMais de R$ 1000: {maisdemil}\nProduto mais barato: {maisbarato}')
  
  
  
  
  
  
  
  
  
