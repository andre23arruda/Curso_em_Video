import random

# ===================== DESAFIO 28 =============================
print('SERA QUE VOCE ACERTA?')
n_pc = random.randint(0,5)
numero = int(input('Digite o numero: '))
if numero == n_pc:
    print('Vc é um descobridor, PARABENS')
else:
    print('Vc é um perdedor')

# =========================== DESAFIO 29 ====================== #
print('\nVOCE é UM BOM MOTORISTA?')
velocidade = int(input('Digite a Velocidade: '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Voce excedeu a velocidade.\nVelocidade de: {}km/h e multa de R${:.2f}'.format(velocidade,multa))
else:
    print('Voce é um bom motorista ;)')


# ==================== DESAFIO 30 =========================== #
print('\nPAR ou IMPAR')
numero = int(input('Digite um numero: '))
if (numero%2 == 0):
    print('O numero {} é par'.format(numero))
else:
    print("O numero {} é impar".format(numero))


# ===================== DESAFIO 31 ====================== #
print('\nPRECO DA VIAGEM')
distancia = int(input('Digite a distancia da viagem: '))
if distancia > 200:
    preco = distancia*0.45
else:
    preco = distancia*0.5
print('O preco da viagem é R${}'.format(preco))


# ============================== DESAFIO 32 ========================= #
print('ANO BISSEXTO')
ano = int(input('Digite o ano: '))
if ano%4 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))


# ===================== DESAFIO 33 =========================== #
print('\nMAIOR E MENOR NUMEROS')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1>n2:
    if n1>n3:
        print('O maior numero é {}'.format(n1))
if n2>n1:
    if n2>n3:
        print('O maior numero é {}'.format(n2))
if n3>n2:
    if n3>n1:
        print('O maior numero é {}'.format(n3))
if n1<n2:
    if n1<n3:
        print('O menor numero é {}'.format(n1))
if n2<n1:
    if n2<n3:
        print('O menor numero é {}'.format(n2))
if n3<n2:
    if n3<n1:
        print('O maior numero é {}'.format(n3))

# =================== DESAFIO 34 ====================== #
print('\nCALCULAR AUMENTO')
salario = int(input('Digite o salario: '))
if salario>1250:
    novo_salario = 1.1*salario;
else:
    novo_salario = 1.5*salario;
print('O salario R${} foi aumentado para R${}'.format(salario,novo_salario))


# ================== DESAFIO 35 ==================== #
print('\nÉ UM TRIANGULO?')
a = int(input('Digite o primeiro lado do triangulo: '))
b = int(input('Digite o segundo lado do triangulo: '))
c = int(input('Digite o terceiro lado do triangulo: '))

if a < (b+c):
    if b < (a+c):
        if c < (b+c):
            print('Sim, é um triangulo')
else:
    print('Só pode ser triangulo em outro mundo')
