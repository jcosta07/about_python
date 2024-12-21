tot = most = cheap = cont = 0
cheapy = ''
while True:
    prod = str(input('Insert the product that you want: '))
    price = int(input('insert his price: '))
    cont += 1
    tot += price
    if price > 1000:
        most += 1
    if cont == 1:
        cheap = price
    elif price < cheap:
        cheap = price
        cheapy = prod
    again = int(input('''[1] Insert more items
    [2] Exit
    Continue?: '''))
    if again == 2:
        print(f'''    Above 1000:{most}
        Total Purchased: {tot}dhs
        Cheaper: {cheapy}-{cheap}dhs''')
        break