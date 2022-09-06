idades = []
alturas = []

for i in range(1 , 6):
    print('%dº Pessoa' % i)
    idade = int(input("Informe a sua idade: "))
    altura = float(input("Informa a sua altura: "))
    idades.append(idade)
    alturas.append(altura)


print("Ordem inversa das idades:")
print(idades[:: -1])

print("Ordem inversa das alturas:")
print(alturas[:: -1])