# =============== DESAFIO 5 ===================== #
numero = int(input('Digite um numero: '))
ant_num = numero - 1
sus_num = numero + 1;
print('O numero {} possui antecessor = {} e sucessor = {} '.format(numero,ant_num,sus_num))

# ============= DESAFIO 6 =================#
numero2 = int(input('Digite um numero: '))
dobro = numero2 * numero2;
triplo = numero2 ** 3;
raiz = numero2 ** 0.5;
print('O numero {} possui dobro = {}, triplo = {} e raiz quadrada = {:.3f}'.format(numero2,dobro,triplo,raiz))


# ================= DESAFIO 7 =================== #
nota1 = int(input('Digite a nota 1: '))
nota2 = int(input('Digite a nota 2: '))
media = (nota1+nota2)/2
print('A media é: {}'.format(media))


# =============== DESAFIO 8 ================= #
print('Programa de converter medidas')
medida = int(input('Entre com a quantidade de metros: '))
print('A medida {} possui {} cm e {} milimetros' .format(medida,medida*100,medida*1000))

# ============= DESAFIO 9 ================= #
print('Calcular tabuada')
numero3 = int(input('Entre com um numero: '))
print('A tabuada de multiplicação é:\n{0} x 1 = {0} \n{0} x 2 = {1} \n{0} x 3 = {2} \n{0} x 4 = {3} \n{0} x 5 = {4}'.format(numero3,numero3*2,numero3*3,numero3*4,numero3*5))

# ============= DESAFIO 10 =================== #
print('Dinheiro na carteira')
dinheiro = int(input('Quanto dinheiro voce tem? '))
dolar = dinheiro/3.27;
print('Voce possui {} reais e pode comprar {:.3f} dólar'.format(dinheiro,dolar))


# ============= DESAFIO 11 ================ #
print('Quantidade de tinta')
largura = int(input('Digite a largura da parede: '))
altura = int(input('Digite a altura da parede: '))
tinta = largura*altura/2
print('A quantidade de tinta necessária para pintar {} m² de parede é {} litros'.format(largura*altura, tinta))


# ================= DESAFIO 12 ===================== #
print('Novo preço')
preco = int(input('Digite o preço do produto'))
print('O novo preco do produto é {}'.format(preco-0.5*preco))


# ================= DESAFIO 13 ======================= #
print('Novo salario')
salario = int(input('Digite o salario atual: '))
print('O novo salario será de {}'.format(salario+0.15*salario))










