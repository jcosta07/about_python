#Crie um algorítmo que leia o salário atual de um funcionário e mostre o seu novo salário, tendo um aumento de 15%
slr = float(input("Insert the value: "))
up = slr + (slr*0.15)
print("Your new salary will be {:.2f} in Dollars, whit that up in 15%".format(up))

