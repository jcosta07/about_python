soma=0
cont=0
for c in range(1,7):
    num=int(input('digite o {}o numero: '.format(c)))
    if num%2==0:
        cont+=1
        soma+=num
print('foram {} pares ao todo, e o seu total foi {}'.format(cont,soma))