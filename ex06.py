#Crie um algorítmo ue leia um número e mostre o seu dobro, triplo e raíz quadrada
n = int(input("Insert a number: "))
d = n * 2
t = n * 3
r = n **(1/2)
print("The double of ", n," is {}, his triple is {}, and the square root is {}".format(d, t, r))