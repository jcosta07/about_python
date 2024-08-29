#Faça um programa que leia a altura e largura de uma parede em metros. Calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo qu cada litro de tinta pinta uma área de 2m**2
height = int(input("Insert the height: "))
width = int(input("insert the width: "))
area = height*width
print("Your area is {}x{}, then {}m2".format(height, width, area))
tin = area/2
print("Will be necessary {}l of paint for that wall".format(tin))