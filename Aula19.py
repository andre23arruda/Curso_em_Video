#### ============= DESAFIO 90 ==================
aluno = {}
aluno['Nome']= input("Nome: ")
print(f"Média de {aluno['Nome']}: ",end = "")
aluno['Media'] = float(input(""))
if aluno['Media'] >= 6:
    aluno['Situacao'] = "APROVADO"
else:
    aluno['Situacao'] = "REPROVADO"
for k,v in aluno.items():
    print(f'{k} é igual a {v}')

## ============= DESAFIO 91 ==================
from random import randrange as rr
from time import sleep
import operator

jogo = {}

for i in range(1,5):
    jogo['jogador'+str(i)] = rr(1,7)
    #print(f'O jogador{str(i)} tirou: {jogo["jogador"+str(i)]}')
print('-='*10 + 'Valores Sorteados' + '-='*10)

for k,v in jogo.items():
    sleep(0.5)
    print(f'O {k} tirou: {v}')
    
jogo_ordem = sorted(jogo.items(), key=operator.itemgetter(1))
sleep(0.5)
print('-='*10 + 'RANKING' + '-='*10)

for j, jogador in enumerate(jogo_ordem):
    sleep(0.5)
    print(f'{j+1}º lugar: {jogador[0]} com {jogador[1]}')

## ============= DESAFIO 92 ==================
import time
pessoa = {}
pessoa['Nome'] = str(input('Nome: '))
ano_atual = int(time.strftime("%Y"))
ano_nascimento = int(input('Ano de nascimento: '))
pessoa['Idade'] = ano_atual - ano_nascimento
pessoa['ctsp'] = int(input('CTSP (zero se não houver): '))
if pessoa['ctsp'] == 0:
    for k,v in pessoa.items():
        print(f'{k}: {v}')
else:
    pessoa['Ano de contratacao'] = int(input('Ano de contratação: '))
    pessoa['Salário'] = float(input('Salário: '))
    pessoa['Idade aposentadoria'] = pessoa['Ano de contratacao'] + 35 - ano_nascimento
    for k,v in pessoa.items():
        print(f'{k}: {v}')

## ============= DESAFIO 93 ==================
jogador = {}
jogador['nome'] = str(input('Nome do jogador:  '))
jogador['gols'] = []
gols_total = 0
n_partidas = int(input('Quantas partidas ' + jogador['nome'] + ' jogou? '))
for i in range(0,n_partidas):
    n_gols = int(input('Quantos gols na partida ' + str(i+1) + '? '))
    jogador['gols'].append(n_gols)
    gols_total += n_gols
jogador['total'] = gols_total
print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'{k}: {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i,g in enumerate(jogador['gols']):
    print(f' ==> Na partida {i+1} {jogador["nome"]} marcou {g}')
print('-='*30)
print(f'{jogador["nome"]} marcou no total {jogador["total"]} gols')

## ============= DESAFIO 94 ==================
p = []
pessoa = {}
n_pessoas = 0
soma_idade = 0
mulheres = []
p_acima_media = []
while True:
    pessoa['Nome'] = input('Nome: ')
    pessoa['Sexo'] = input('Sexo (F/M): ').upper()
    while not(pessoa['Sexo'] in 'mMfF'):
        pessoa['Sexo'] = input('Sexo (F/M): ').upper()
    pessoa['Idade'] = int(input('Idade: '))
    soma_idade += pessoa['Idade']
    n_pessoas += 1
    p.append(pessoa.copy())
    if pessoa['Sexo'] in 'fF':
        mulheres.append(pessoa['Nome'])
    continuar = input('Deseja continuar (S/N)? ')
    while not(continuar in 'sSnN'):
        continuar = input('Deseja continuar (S/N)? ')
    if continuar in 'nN':
        break
print('-='*30)
print(f'- Foram cadastradas {n_pessoas} pessoas')
media_idade = soma_idade/n_pessoas
print(f'- Media da idade: {media_idade} anos')
print(f'- Mulheres: {mulheres} \n')
print(f'Pessoas com idade acima da media:')
for i in range (0,n_pessoas):
    if p[i]['Idade'] > media_idade:
        p_acima_media.append(p[i]['Nome'])
        print(f'- {p[i]["Nome"]} com {p[i]["Idade"]}')
#print(f'Pessoas com idade acima da media: {p_acima_media}')
print('\nENCERRADO')


## ============= DESAFIO 95 ==================
jogadores = []
while True:
    jogador = {}
    jogador['nome'] = str(input('Nome do jogador:  '))
    jogador['gols'] = []
    gols_total = 0
    n_partidas = int(input('Quantas partidas ' + jogador['nome'] + ' jogou? '))
    for i in range(0,n_partidas):
        n_gols = int(input('Quantos gols na partida ' + str(i+1) + '? '))
        jogador['gols'].append(n_gols)
        gols_total += n_gols
    jogador['total'] = gols_total
    jogadores.append(jogador.copy())
    continuar = input('Deseja continuar (S/N)? ')
    print('-'*30)
    while not(continuar in 'sSnN'):
        continuar = input('Deseja continuar (S/N)? ')
    if continuar in 'nN':
        break
print('-='*30)
print('cod \t nome \t gols \t total')
print('-'*30)
for i in range(0,len(jogadores)):
    print(f'{i+1} \t {jogadores[i]["nome"]} \t {jogadores[i]["gols"]} \t {jogadores[i]["total"]}')
while True:
    print('-'*30)
    cod = int(input('Mostrar dados de qual jogador? '))
    while cod > len(jogadores) or cod < 1:
        print(f'ERRO! Não existe jogador com codigo {cod}. Tente novamente')
        print('-'*30)
        cod = int(input('Mostrar dados de qual jogador? '))
    print(f'DADOS DO JOGADOR {jogadores[cod-1]["nome"]}')
    for i,gols in enumerate(jogadores[cod-1]["gols"]):
        print(f'No jogo {i+1} fez {gols}')
    continuar = input('Deseja continuar (S/N)? ')
    print('-'*30)
    while not(continuar in 'sSnN'):
        continuar = input('Deseja continuar (S/N)? ')
    if continuar in 'nN':
        break
