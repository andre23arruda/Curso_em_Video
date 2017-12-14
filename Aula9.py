# =================== DESAFIO 22 ===================== #
nome = input('Digite o nome: ')
nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
nome_separada = nome.split()
n_caracteres = len(''.join(nome_separada))
n_primeiro_nome = len(nome_separada[0])
print('Nome maiusculo {}\nNome minusculo: {}\nNumero de letras: {}\nNumero de letras do primeiro nome: {}\n'.format(nome_maiusculo,nome_minusculo,n_caracteres,n_primeiro_nome))



# ====================== DESAFIO 23 ====================== #
numero = input('Digite um numero de 0 a 9999: ')
print('Unidade: {}\nDezena: {}\nCentena: {}\nMilhar: {}'.format(numero[3],numero[2],numero[1],numero[0]))


# ====================== DESAFIO 24 ======================= #
cidade = input('Digite o nome da cidade: ')
cidade_m = cidade.upper()
print('A cidade começa com SANTO?\n{}'.format('SANTO'in cidade_m[0:5]))


# ==================== DESAFIO 25 ========================= #
nome2 = input('Digite o nome: ')
nome2_m = nome2.upper()
print('A pessoa possui o nome SILVA?\n{}'.format('SILVA'in nome2_m))


# ====================== DESAFIO 26 =========================== #
frase = input('Digite uma frase: ')
frase_m = frase.upper()
qtd_a = frase_m.count('A')
pos1_a = frase_m.find('A')
pos_last_a = frase_m.rfind('A')
print('Numero de vezes A: {}\nPrimeira posicao de A: {}\nUltima posicao de A:{}'.format(qtd_a,pos1_a,pos_last_a))


# ================== DESAFIO 27 ============================== #
nome3 = input('Digite o nome: ')
nome3_fatiado = nome3.split();
print('Primeiro nome: {}\nUltimo nome: {}'.format(nome3_fatiado[0],nome3_fatiado[len(nome3_fatiado)-1]))




