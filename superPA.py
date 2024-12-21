n = int(input('insert the start: '))
r = int(input('insert the reason: '))
t = n
count = 0
mais = 10
total = 0
while mais != 0:
    total += mais
    while count < total:
         count += 1
         print(n, " -> " if count < mais else ".", end = " ")
         n += r
    print('PAUSA')
    mais = int(input('insira mais se quiser: '))
print(f'O total foi {total}')