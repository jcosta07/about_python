from random import randint
count = p = c = 0
print('='*10, 'PAR OU IMPAR', '='*10)
while True:
    com = randint(0,999)
    print('-'*20)
    esc = int(input('''
    [1]PAR
    [2]ÍMPAR
    [3]SAIR
    Par(1)/Impar(2)/Sair(3)?: '''))
    if esc == 1:
        player = int(input('insert a number: '))
        print('+'*20)
        print(f'AI goes to {com}')
        print(f'PLAYER goes to {player}')
        r = com + player
        print(f'The result is {r}')
        if r % 2 == 0:
            print('PLAYER Wins!')
            p += 1
        elif r % 2 == 1:
            print('AI Wins!')
            c += 1
        print('+'*20)
    if esc == 2:
        player = int(input('insert a number: '))
        print('+'*20)
        print(f'AI goes to {com}')
        print(f'PLAYER goes to {player}')
        r = com + player
        print(f'The result is {r}')
        print('+'*20)
        if r % 2 == 1:
            print('PLAYER Wins!')
            p += 1
        elif r % 2 == 0:
            print('AI Wins!')
            c += 1
    if esc == 3:
        print('÷'*20)
        print('SAINDOOOOOO...!')
        print(f'''        P1: {p} Points
        IA: {c} Points''')
        print('÷'*20)
        break
    print('-'*20)