import random
num = random.randint(1, 10)
eu = int(input('insert a number: '))
tent = 0
while eu != num:
    print(f'Error! COM thinks {num} and you try {eu}')
    num = random.randint(1, 10)
    eu = int(input('try again: '))
    tent += 1
print(f'''-------YOU DID IT!!-------
COM thought {num} and you {eu}''')
print(f'You tried {tent} times kkkk')