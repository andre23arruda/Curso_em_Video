# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:18:46 2019

@author: André Arruda
"""

#%% Desafio 107
from cev import moeda
p = float(input("Digite o preço: R$"))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
print(f'Diminuindo 25%, temos {moeda.diminuir(p,25)}')

#%% Desafio 108
from cev import moeda
p = float(input("Digite o preço: R$"))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Diminuindo 25%, temos {moeda.moeda(moeda.diminuir(p,25))}')

#%% Desafio 109
from desafio109 import moeda
p = float(input("Digite o preço: R$"))
print(f'A metade de {moeda.moeda(p)} é {(moeda.metade(p,False))}')
print(f'O dobro de {moeda.moeda(p)} é {(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {(moeda.aumentar(p,10))}')
print(f'Diminuindo 25%, temos {(moeda.diminuir(p,25))}')
#%% Desafio 110
from desafio109 import moeda
preco = float(input('Digite o preço: R$'))
moeda.resumo(preco, 80, 35, formatacao = True)

#%% Desafio 111
# Pasta criada e com todas as funções

#%% Desafio 112
from utilidadesCeV import dado, moeda
p = dado.leiaDinheiro("Digite o preço: R$")
moeda.resumo(p, 80, 35, formatacao = True)

