def addPerson():
    f = open('G:\Meu Drive\CODIGOS\PYTHON\pythonCeV\Aula23\\register.txt', "a+") # adicionando linha
    print('-'*30)
    print(f'Novo Cadastro'.center(30))
    print('-'*30)
    name = validateName().upper()
    age = validateAge()
    f.write(f'\n{name}'.ljust(20))
    f.write(f'{age} anos'.rjust(5))
    f.close()


def validateName(texto = 'Digite um nome: '):
    while True:
        n = input(texto)
        if n == '':
            n = 'Sem nome'
            print(f'\x1b[6;30;41m O usuario preferiu não informar nome\x1b[0m')
        return n


def validateAge(texto = 'Digite a idade: ', showNumber = False):
    while True:
        n = input(texto).strip()
        if n == '':
            n = 0
            print(f'\x1b[6;30;41m O usuario preferiu não informar idade\x1b[0m')
        try:
            int(n)
            return int(n)
        except Exception as erro:
            print(f'\x1b[6;30;41m {erro.__class__}\x1b[0m')


def printRegister():
    f = open("G:\Meu Drive\CODIGOS\PYTHON\pythonCeV\Aula23\\register.txt", "r")
    if f.mode == 'r':
        contents =f.read()
        print('-'*30)
        print(f'Pessoas Cadastradas'.center(30))
        print('-'*30)
        print(contents)
        f.close()
        
        
def validateChoice(texto = 'Sua opção: '):
    while True:
        n = input(texto)
        if n == '':
            n = 2
            print(f'\x1b[6;30;41m O usuario preferiu não informar idade\x1b[0m')
            print(f'\x1b[6;30;41m Saindo do sistema \x1b[0m')
        try:
            n = int(n)
            if n>=1 and n<4:
                return int(n)
            else:
                print(f'\x1b[6;30;41m Digite um número válido \x1b[0m')
        except:
            print(f'\x1b[6;30;41m Digite um número válido \x1b[0m')
        
def menuRegister():
    from time import sleep
    while True:
        print('-'*30)
        print(f'Menu Principal'.center(30))
        print('-'*30)
        print(f'1 - Ver pessoas cadastradas')
        print(f'2 - Cadastrar nova pessoa')
        print(f'3 - Sair do Sistema')
        print('-'*30)
        choice = validateChoice()
        if choice == 1:
            printRegister()
            sleep(1.2)
        elif choice == 2:
            addPerson()
            sleep(1.2)
        else:
            print(f'\x1b[6;39;41m Saindo do sistema \x1b[0m')
            print(f'\x1b[6;39;41m ----- Até Logo ----- \x1b[0m')
            sleep(1.2)
            break
            