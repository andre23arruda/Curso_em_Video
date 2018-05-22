# =================== DESAFIO 72 ===================== #
tupla = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
numero = -1
while numero < 0 or numero > 10:
    numero = int(input('Digite um numero de 0 a 10: '))
print(f'Voce digitou  {tupla[numero]}')

# =================== DESAFIO 73 ===================== #
times = ('FLAMENGO','CONRINTHIANS','SAO PAULO', 'CRUZEIRO','CHAPECOENSE','VASCO','INTERNACIONAL')
print(f'Primeiros {times[:5]}')
print(f'Ultimos {times[-4:]}')
chape = times.index('CHAPECOENSE') + 1
print(f'Posicao CHAPE: {chape}')
print(f'Ordem alfabetica: {sorted(times)}')

# =================== DESAFIO 74 ===================== #
import random
tupla = tuple(random.sample(range(10), 5))
minimo = min(tupla)
maximo = max(tupla)
print('Numeros sorteados: ',end = '')
for numero in tupla:
    print(numero,end = ' ')
print(f'\nMinimo: {minimo}')
print(f'Maximo: {maximo}')

# =================== DESAFIO 75 ===================== #
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
n3 = int(input('Digite mais um numero: '))
n4 = int(input('Digite o ultimo numero: '))
tupla = (n1,n2,n3,n4)
print(f'Voce digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)}')
tem3 = tupla.count(3)
if tem3 == 0:
    print('O valor 3 nao foi digitado')
elif tem3 == 1:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}ª posicao')
else:
    print('O valor 3 apareceu em mais de uma posicao')
print('Os valores pares digitados foram:',end = ' ')
for numeros in tupla:
    if numeros%2 == 0:
        print(numeros,end = ' ')
 
# =================== DESAFIO 76 ===================== #
tupla = ('Lapis',1.50,'Borracha',2.00,'Casaco',50.00,'Tenis',100)
print('======================== LISTAGEM DE PREÇOS ============================')
for i in range(0,len(tupla),2):
    print('{:.<30} R${:10.2f}'.format(tupla[i],tupla[i+1]))

# =================== DESAFIO 77 ===================== #
tupla = ('andre','luiz')
for i in tupla:
    palavra = i.upper()
    cont_a = palavra.count('A')
    cont_e = palavra.count('E')
    cont_i = palavra.count('I')
    cont_o = palavra.count('O')
    cont_u = palavra.count('U')
    if cont_a + cont_e + cont_i + cont_o + cont_u == 0:
        print(f'\nA palavra {palavra} nao possui vogais')
    else:
        print(f'\nA palavra {palavra} possui:', end = ' ')
        for letra in palavra:
            if letra == 'A':
                print('a', end = ' ')
            if letra == 'E':
                print('e', end = ' ')
            if letra == 'I':
                print('i', end = ' ')
            if letra =='O':
                print('o', end = ' ')
            if letra == 'U':
                print('u', end = ' ')




