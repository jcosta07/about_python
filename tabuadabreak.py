n = int(input('insert a number: '))
while True:
    print('='*20)
    for c in range(1, 13):
        m = n * c
        if n < 0:
            print('Número Negativo Encontrado, PROGRAMA ENCERRADO!')
            break
        print(f'{n}×{c}={m}')
    n = int(input('insert another number: '))