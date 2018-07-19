# --------------- DESAFIO 84 ------------------------
lista = list()
dados = list()
pesos = list()

cont = 0

while True:
    cont +=1
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    pesos.append(dados[1])
    lista.append(dados[:])
    dados.clear()
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar in 'nN':
        break
    
maior_peso = max(pesos)
menor_peso = min(pesos)

print('-='*30)

print(f'Ao todo, voce cadastrou {cont} pessoas')
print(f'O maior peso foi de {maior_peso}Kg. Peso de: ',end = '')
for i in lista:
    if i[1] == maior_peso:
        print(f'[{i[0]}]',end = ' ')

print(f'\nO menor peso foi de {menor_peso}Kg. Peso de: ',end = '')
for i in lista:
    if i[1] == menor_peso:
        print(f'[{i[0]}]',end = ' ')
    
# --------------- DESAFIO 85 ------------------------
lista = [[],[]]
for i in range(0,7):
    print(f'Digite o {i+1}o valor: ', end = '')
    num = int(input(''))
    if num%2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
        
print('-='*30)
        
print(f'Os valores pares digitados foram: {sorted(lista[0])}')
print(f'Os valores impares digitados foram: {sorted(lista[1])}')


## --------------- DESAFIO 86 ------------------------
matriz = [[],[],[]]
for i in range(0,3):
    for l in range(0,3):
        print(f'Digite um valor para [{i},{l}]: ',end = '')
        matriz[i].append(int(input('')))
print('-='*30)
for i in range(0,3):
    for l in range(0,3):
        print(f'[ { matriz[i][l]} ]',end = '')
    print('\n',end = '')

# --------------- DESAFIO 87 ------------------------
matriz = [[],[],[]]
soma_par = 0
soma_3_coluna = 0
for i in range(0,3):
    for l in range(0,3):
        print(f'Digite um valor para [{i},{l}]: ',end = '')
        numero = int(input(''))
        matriz[i].append(numero)
        if numero%2 == 0:
            soma_par = soma_par+numero
        if l == 2:
            soma_3_coluna = soma_3_coluna + numero
maior_2_linha = max(matriz[1])

print('-='*30)
for i in range(0,3):
    for l in range(0,3):
        print(f'[ { matriz[i][l]} ]',end = '')
    print('\n',end = '')
    
print('-='*30)
print(f'A soma dos valores pares é {soma_par}')
print(f'A soma dos valores da terceira coluna é {soma_3_coluna}')
print(f'O maior valor da segunda linha é {maior_2_linha}')

# --------------- DESAFIO 88 ------------------------
from random import randrange as rr
import time

numeros = list()
print('-'*30)
print('{:^30}'.format('JOGA NA MEGA SENA'))
n_jogos = int(input('Quantos jogos voce quer que eu sorteie? '))
print('-='*3 + ' SORTEANDO {} JOGOS '.format(n_jogos) + '-='*3)

for i in range(0,n_jogos):
    numero_anterior = 0
    for l in range(0,6):
        numero_atual = rr(1,61)
        while numero_atual in numeros:
            numero_atual = rr(1,61)
        numeros.append(numero_atual)
        numero_anterior = numero_atual
    print(f'Jogo {i+1}: {sorted(numeros)}')
    numeros.clear()
    time.sleep(0.5)
    
print('-='*5 + ' BOA SORTE ' + '-='*5)


# --------------- DESAFIO 89 ------------------------
lista = list()

while True:
  aluno = list()
  nome = input('NOME: ')
  aluno.append(nome[:])
  notas = [float(input('Nota1: ')), float(input('Nota2: '))]
  aluno.append(notas[:])
  lista.append(aluno[:])
  aluno.clear()
  continuar = input('Quer continuar? [S/N] ').upper()
  if continuar in 'nN':
    break

print('-='*30) 
print('No.\t NOME \t MÉDIA')
print('-'*30) 

for i,aluno in enumerate(lista):
  print(f'{i} \t {aluno[0]} \t {(aluno[1][0] + aluno[1][1])/2}')

print('-'*30) 

while True:
  escolha = input('Deseja visualizar a nota de algum aluno? [S/N]').upper()
  if escolha in 'nN':
    break
  i = int(input('Qual aluno? '))
  print(f'Notas de {lista[i][0]} são {lista[i][1]}')
  print('-'*30)
print('FINALIZANDO...\n<<< VOLTE SEMPRE >>>')

