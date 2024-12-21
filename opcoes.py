num1 = int(input('insert a number: '))
num2 = int(input('insert another number: '))
opcao = 0
resul = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3]maior valor
    [4]novos numeros
    [5]sair''')
    opcao = int(input('Escolha uma opcao: '))
    if opcao == 1:
        resul = num1 + num2
        print('\n')
        print(f'''---{num1}+{num2}={resul}---''')
    elif opcao == 2:
        resul = num1 * num2
        print('\n')
        print(f'''---{num1}x{num2}={resul}---''')
    elif opcao == 3:
        if num1 > num2:
            resul = num1
            print(f'{resul} is higher')
        elif num1 < num2:
            resul = num2
            print(f'{resul} is higher')
        else:
            print('there are no higher, both are equal!')
    elif opcao == 4:
        num1 = int(input('again, insert the first number: '))
        num2 = int(input('again, insert the sconde number: '))
print('Encerrando...')