print('=' *30)
print('{:^30}'.format('BANCO'))
print('=' *30)
valor = int(input('insert a value: '))
cash = 50
count = 0
while True:
    if valor >= cash:
        valor -= cash
        count += 1
    else:
        if count > 0:
            print(f'total de  {count} notas de {cash}')
        if cash == 50:
            cash = 20
        elif cash == 20:
            cash = 10
        elif cash == 10:
            cash = 1
        count = 0
        if valor == 0:
            break