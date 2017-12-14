# ============ DESAFIO 16 ================== #
import math
import random

numero = float(input('Digite um numero: '))
inteiro = math.floor(numero)
print('O numero {} tem a part inteira {}'.format(numero,inteiro))


# ============ DESAFIO 17 ================ #
c1 = int(input('Digite o valor do cateto oposto: '))
c2 = int(input('Digite o valor do cateto adjacente: '))
print('A hipotenusa tem valor de {:.2f}'.format(math.sqrt(c1*c1 + c2*c2)))

# ============= DESAFIO 18 ============== #
angulo = int(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo));
cosseno = math.cos(math.radians(angulo));
tangente = math.tan(math.radians(angulo));
print('O angulo {:.1f} possui seno {:.1f}, cosseno {:.1f} e tangente {:.1f}'.format(angulo,seno,cosseno,tangente))


# ============= DESAFIO 19 ================ #
a1 = input('Digite o nome do aluno 1: ');
a2 = input('Digite o nome do aluno 2: ');
a3 = input('Digite o nome do aluno 3: ');
a4 = input('Digite o nome do aluno 4: ');
lista = [a1,a2,a3,a4]
sorteio = random.choice(lista)
print('O aluno {} foi sorteado'.format(sorteio))


# =============== DESAFIO 20 =============== #
random.shuffle(lista)
print(lista);



