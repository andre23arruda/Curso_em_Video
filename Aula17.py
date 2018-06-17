### =================== DESAFIO 78 ===================== #
##lista = []
##for i in range(0,5):
##    print(f'Digite um valor para a posicao {i}: ',end = '')
##    lista.append(int(input('')))
##maior = max(lista)
##menor = min(lista)
##print(lista)
##print(f'Maior: {maior}, posicao: ',end = '')
##for pos, i in enumerate(lista):
##    if i == maior:
##        print(pos,end = ' ')
##print('')
##print(f'Menor: {menor}, posicao: ',end = '')
##for pos, i in enumerate(lista):
##    if i == menor:
##        print(pos,end = ' ')

### =================== DESAFIO 79 ===================== #
##lista = []
##escolha = 'S'
##while escolha == 'S':
##    num = int(input('Digite um valor: '))
##    if num in lista:
##        print('Valor duplicado, não vou adicionar')
##    else:
##        lista.append(num)
##        print('Numero adicionado com sucesso:!')
##    escolha = input('Deseja continuar? [S/N] ').upper()
##print(sorted(lista))

### =================== DESAFIO 80 ===================== #
##lista = []
##lista.append(int(input('Digite um valor: ')))
##print('Valor adicionado na posicao 0')
##for i in range(0,4):
##    maximo = max(lista)
##    minimo = min(lista)
##    num = int(input('Digite um valor: '))
##    if num<=minimo:
##        lista.insert(0,num)
##        print('Valor adicionado na posicao 0')
##    elif num>=maximo:
##        lista.append(num)
##        print(f'Valor adicionado na posicao {len(lista)-1}')
##    else:
##        pos = 0
##        valor = lista[0]
##        while num>valor:
##            pos = pos + 1
##            valor = lista[pos]
##        lista.insert(pos,num)
##        print(f'Valor adicionado na posicao {pos}')
##print(lista)

### =================== DESAFIO 81 ===================== #
##lista = []
##escolha = 'S'
##cont = 0
##while escolha == 'S':
##    num = int(input('Digite um valor: '))
##    lista.append(num)
##    print('Numero adicionado com sucesso!')
##    cont = cont+1
##    escolha = input('Deseja continuar? [S/N] ').upper()
##lista.sort(reverse = True)
##print(lista)
##print(f'Numeros digitados: {cont}')
##if 5 in lista:
##    print('O numero 5 está na lista')
##else:
##    print('O numero 5 NÃO esta na lista')
    
### =================== DESAFIO 82 ===================== #
##lista = []
##par = []
##impar = []
##escolha = 'S'
##while escolha == 'S':
##    num = int(input('Digite um valor: '))
##    lista.append(num)
##    if num%2 == 0:
##        par.append(num)
##    else:
##        impar.append(num)
##    print('Numero adicionado com sucesso!')
##    escolha = input('Deseja continuar? [S/N] ').upper()
##print(f'Lista completa: {lista}')
##print(f'Pares: {par}')
##print(f'Impares: {impar}')

### =================== DESAFIO 83 ===================== #
expressao = input('Digite a expressao: ')
cont1 = expressao.count('(')
cont2 = expressao.count(')')
if cont1 == cont2:
    print('VALIDO!!!')
else:
    print('EQUIVOCADO!!!')

    
    


