n = int(input('insert a number: '))
count = gt = lt = av = tot = 0
print(n)
count += 1
tot += n
again = 1
while again == 1:
    if count == 1:
        gt = n
        lt = n
    elif gt < n:
        gt = n
    else:
        lt > n
        lt = n
    count += 1
    tot += n
    n = int(input("insert another number: "))
    again = int(input('''[1] yes
[2] no
Do you want to repeat?: '''))
av = tot / count
print(f'''Average: {av}
Higher Number: {gt}
Lower Number: {lt}
Total: {count} number''')