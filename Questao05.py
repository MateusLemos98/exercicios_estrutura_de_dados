num = int(input("Digite um número inteiro:"))
lista = []
print(num)

for i in range(num + 1):
     if i % 2 == 1 and i != 2:
         lista.append(i)


print(lista)

