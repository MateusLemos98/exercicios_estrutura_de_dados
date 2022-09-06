def reverso(num):
    return str(num[:: -1])

num = str(input("Digite um número: ")).strip()
print(reverso(num))

