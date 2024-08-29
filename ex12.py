#Crie um algorítmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto
prod = int(input("insert the product value: "))
per = prod - (prod * 0.05)
print("The original price is {} Euros, but, with the 5% of descount, you must to pay {}Euros".format(prod, per))