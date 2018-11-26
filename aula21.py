# --------------------- DESAFIO 101 -------------------------- #
def voto(ano = 0):
    import datetime as dt
    anoAtual = dt.date.today().year
    idade = anoAtual - ano
    if idade < 16:
        v = "Com " + str(idade) + " anos o voto é negado"
    elif 16 <= idade < 18 or idade >= 65:
        v = "Com " + str(idade) + " anos o voto é opcional"    
    else:
        v = "Com " + str(idade) + " anos o voto é obrigatório"    
    return v

print('-'*30)
ano = int(input('Digite o ano de nascimento: '))
print('-'*30)
print(f'{voto(ano)}')


# --------------------- DESAFIO 102 -------------------------- #
def fatorial(n,show = False):
    """
    Função que calcula o fatorial de um numero.
    INPUTS:
        - n = numero que será calculado o fatorial
        - show = parametro (1 ou 0) para exibir o calculo inteiro do fatorial
                 default  = 0
                 1 = mostra o calculo
    OUTPUTS:
        - f = valor do fatorial calculado
    """
    i = n
    fatorial = 1 
    while i>=1:
        fatorial *= i
        if show:
            print(f'{i}',end = '')
            if i == 1:
                print(f' = {fatorial}')
            else:
                print(f' x ',end = '')
        else:
            print(f'{fatorial}')
        i -= 1
    return fatorial

help(fatorial)

print('-'*30)
f = fatorial(10,True)


# --------------------- DESAFIO 103 -------------------------- #
#def ficha(jogador, gols):
    """
    Função que exibe o nome do jogador e quantos gols marcados pelo mesmo
    INPUTS:
        - jogador = nome do jogador
                    default = desconhecido
        - gols = numero de gols marcados pelo jogador
                 default  = 0
                 
    OUTPUTS:
    """
    if len(jogador) == 0:
        jogador = '<desconhecido>'
    if len(gols) == 0:
        gols = 0
    else:
        gols = int(gols)
    print(f'O jogador {jogador} marcou {gols} gol(s)')

print('-'*30)
j = input('Nome do jogador: ')
g = input('Número de gols: ')
ficha(j,g)


# --------------------- DESAFIO 104 -------------------------- #
def leiaInt(texto):
    while True:
        n = input(texto)
        if n.isnumeric() and (int(n) - float(n)) == 0:
            break
        else:
            print('ERRO! Digite um número inteiro válido')
    return n

n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}')

# --------------------- DESAFIO 105 -------------------------- #
def notas(*n, sit=False):
    nNotas = len(n)
    maior = max(n)
    menor = min(n)
    media = 0
    soma = 0
    for z in n:
        soma += z
    media = soma/nNotas
    if sit == True:
        if media >= 7.5:
            situacao = "BOA"
        elif media >=6 and media < 7.5:
            situacao = 'RAZOAVEL'
        else:
            situacao = "RUIM"
        d = {'Total': nNotas,
             'Maior': maior,
             'Menor': menor,
             'Media': media,
             'Situacao':situacao}
    else:
        d = {'Total': nNotas,
             'Maior': maior,
             'Menor': menor,
             'Media': media}
    return d
    
d = notas(5,6,3,2,1,4,sit = False)
print(d)








