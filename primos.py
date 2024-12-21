n = int(input('insert a number: '))
for c in range(1,n+1):
    print(c, end = ' ')
if n % 2 == 0:
        print('Não é primo')
else:
        print('É primo')