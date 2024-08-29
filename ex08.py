#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e/ou milímetros
m = float(input("How many of meters: "))
cm = m * 100
mm = m * 1000
print("{}m, this is the same that {}cm, and {}mm too".format(m, cm, mm))
