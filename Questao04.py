ano = int(input("Digite o ano que deseja:"))

if (ano%4 == 0 and ano%100 != 0) or (ano%400 == 0):
    print("O ano ", ano ,", é um ano Bissexto")
else:
    print("O ano ", ano ,", não é um ano Bissexto")