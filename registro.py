m = 0
f = 0
masvelho = 0
nomevelho = ''
novinha = 0
pessoas = 0
idades = 0
for dado in range (1, 5):
    print(f'------------{dado}ª pessoa------------')
    nome = str (input(f"insira a {dado}ª pessoa: ")).title()
    idade = int (input("insira a sua idade: "))
    genero = input("Masculino ou Femenino?: ").lower()
    print('==/'*12)
    pessoas += 1
    if idade != 0 :
        idades += idade
    if genero == "m":
        m += 1
        if dado == 1:
            masvelho = idade
            nomevelho = nome
        elif idade > masvelho:
            masvelho = idade
            nkmevelho = nome
    if genero == "f":
        f += 1
        if idade < 20:
            novinha += 1
print(f"Total de pessoas: {pessoas}")
print(f'''Total de Homens: {m}
Total de Mulheres: {f}''')
print(f'''O mais homem mais velho tem: {masvelho}
O Homem mais velho se chama:{nomevelho}
Mulheres abaixo dos 20: {novinha}''')
print(f'Média de idade: {idades / dado}')