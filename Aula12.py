import datetime
import random
# ==================== DESAFIO 36 ======================== #
print('VAI COMPRAR UM CASA?')
casa = int(input('Digite o valor da casa: '))
salario = int(input('Digite seu salario: '))
anos = int(input('Digite em quantos anos pretende pagar: '))
prestacao = casa/(12*anos)
if prestacao>0.3*salario:
    print('Emprestimo negado :(')
else:
    print('Voce vai comprar sua casa sim ;)')


# ======================= DESAFIO 37 ======================== #
print('\nCONVERSÃO DE BASES')
numero = int(input('Digite um numero:'))
base = int(input('Deseja converter para qual base?\nEntre com: \n1 - Binario\n2 - Octal \n3 - Hexadecimal\n'))
lista_numero = [bin(numero),oct(numero),hex(numero)]
lista = ['binario','octal','hexadecimal']
if base == 1:
    print('O numero {} é igual a {} em {}'.format(numero,lista_numero[0],lista[0]))
elif base == 2:
    print('O numero {} é igual a {} em {}'.format(numero,lista_numero[1],lista[1]))
else:
    print('O numero {} é igual a {} em {}'.format(numero, lista_numero[2], lista[2]))


# ========================== DESAFIO 38 ========================= #
print('\nCONFERIR NUMEROS')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1>n2:
    print('{} é maior que {}'.format(n1,n2))
elif n1 < n2:
    print('{} é maior que {}'.format(n2, n1))
else:
    print('Os numeros sao iguais')

# ======================= DESAFIO 39 ============================ #
print('\nALISTAMENTO')
ano = int(input('Em qual ano voce nasceu?'))
ano_atual = datetime.date.today().year
if ano_atual - ano == 18:
    print('Está na hora de alistar')
elif ano_atual - ano < 18:
    print('Faltam {} anos para se alistar'.format(18 -(ano_atual-ano)))
else:
    print('Voce se alistou ha {} anos'.format(ano_atual-ano-18))


# =================== DESAFIO 40 ===================== #
print('\n SITUAÇÃO DO ALUNO')
n1 = int(input('Entre com a primeira nota: '))
n2 = int(input('Entre com a segunda nota: '))
media = (n1+n2)/2
if media < 5:
    print('Aluno reprovado')
elif media>=5 and media <= 6.9:
    print('Aluno de recuperação')
else:
    print('Aluno aprovado')


# ======================== DESAFIO 41 ==================== #
print('\nCATEGORIA NATAÇÃO')
ano = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.date.today().year
if ano_atual - ano <= 9:
    print('Categoria: MIRIM')
elif ano_atual - ano >9 and ano_atual - ano <= 14:
    print('Categoria: INFANTIL')
elif ano_atual - ano > 14 and ano_atual - ano <= 19:
    print('Categoria: JUNIOR')
elif ano_atual - ano >19 and ano_atual - ano <= 20:
    print('Categoria: SENIOR')
else:
    print('Categoria: MASTER')

# ========================= DESAFIO 42 ============================ #
a = int(input('Digite o valor do lado a: '))
b = int(input('Digite o valor do lado b: '))
c = int(input('Digite o valor do lado c: '))
if a<b+c and b<a+c and c<a+b:
    if a == b and b == c:
        print('Triangulo equilatero')
    elif (a==b and b != c) or (a==c and c !=b) or (c==b and b != a):
        print('Triangulo isosceles')
    elif (a!=b and a!=c and b!=c):
        print('Trianculo escaleno')
else:
    print('Nao é triangulo')


# ================= DESAFIO 45 ====================== #
print('LETS PLAY')
lista = [1,2,3]
pc = random.choice(lista)
usuario = int(input('Pedra, Papel ou Tesoura?\n1 - Pedra\n2 - Papel\n3 - Tesoura'))
if usuario - pc == 0:
    print('O PC jogou {}\nEmpatou'.format(pc))
elif (usuario - pc == -1) or (usuario - pc == 2):
    print('O PC jogou {}\nVoce Perdeu'.format(pc))
elif (usuario - pc == 1) or (usuario - pc == -2):
    print('O PC jogou {}\nVoce Ganhou'.format(pc))
print('FIM DE JOGO')





