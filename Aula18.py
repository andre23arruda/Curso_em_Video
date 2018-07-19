lista = list()

while True:
  aluno = list()
  nome = input('NOME: ')
  aluno.append(nome)
  notas = [int(input('Nota1: ')), int(input('Nota2: '))]
  aluno.append(notas)
  lista.append(aluno)
  aluno.clear()
  continuar = input('Quer continuar? [S/N] ').upper()
  if continuar in 'nN':
    break

print('-='*30) 
print('No.\t NOME \t MÉDIA')
print('-'*30) 

for i,aluno in enumerate(lista):
  print(f'{i} \t {aluno[0]} \t {(aluno[1][0] + aluno[1][1])/2}')

print('-'*30) 

while True:
  escolha = input('Deseja visualizar a nota de algum aluno? [S/N]').upper()
  if escolha in 'nN':
    break
  i = int(input('Qual aluno? '))
  print('Notas 


