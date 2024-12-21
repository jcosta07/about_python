n = int(input('insert a number: '))
totalsum = 0
totalcount = 0
while n != 999:
    totalcount += 1
    totalsum += n
    n = int(input('insert another number[999 to STOP]: '))
print(f'You insert {totalcount} times and in total it was {totalsum} \n STOP!')
    