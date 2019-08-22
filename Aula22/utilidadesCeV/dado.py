# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:37:44 2019

@author: André Arruda
"""

def leiaDinheiro(frase):
    """ Função de validação de dado para verificar se é numero de preco
        INPUTS:
            p: preço
        OUTPUTS:
            True (se for numero) ou False (se nao for numero) 
    """
    while True:
        p = str(input(frase))
        if p.isnumeric():
            break
        else:
            p = p.replace(',','.')
            caracteres = p.split('.')
            if len(caracteres)<2:
                print(f'ERRO: "{p}" NÃO É UM PREÇO VÁLIDO!')
            else:
                p1 = caracteres[0]
                p2 = caracteres[1]
                if p1.isnumeric() and p2.isnumeric():
                    break
                else:
                    print(f'ERRO: "{p}" NÃO É UM PREÇO VÁLIDO!')
    return float(p)