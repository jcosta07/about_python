n = int(input('insert a number: '))
count = 1
tot= n
while True:
    n = int(input('insert another number: '))
    if n == 999:
        break
    count += 1
    tot += n
print(f'''Total: {tot}
Counting: {count}''')