n = int(input("how many do you want: "))
t1 = 0
t2 = 1
count = 0
print(f'{t1}=> {t2}', end = '')
while count < n - 2:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    count += 1
    print('=>',t3, end = '')