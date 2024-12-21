youth = men = girls = 0
print('-'*10,'Data Entry','-'*10)
while True:
    print('-'*20)
    gen = str(input('''    [M] Male
    [F] Female
    Select your genre: ''')).upper()
    age = int(input('input your age: '))
    print('-'*20)
    if gen == 'M':
        men += 1
    elif gen == 'F':
        if age < 20:
            girls += 1
    else:
        print('Unknown, Try Again')
    if age < 18:
        youth += 1
    print('~'*17)
    again = int(input('''[Any number] Yes
    [1] No
    Do you want to Continue?: '''))
    print('~'*17)
    if again == 1:
        print('-'*20)
        print(f'''Data Colected!
        Men: {men}
        Female under 20: {girls}
        People under 18: {youth}''')
        print('-'*20)
        break