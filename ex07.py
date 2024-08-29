#Crie um programa que leia as notas de um aluno e calcule a sua média
n = int(input("Insert your first note: "))
n2 = int(input("Insert your second note: "))
n3 = int(input("Insert your third note: "))
m = (n+n2+n3)//3
print("Based in your last rate, your average is {}".format(m))