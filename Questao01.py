nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota:'))
nota3 = float(input('Digite sua terceira nota:'))

media = (nota1 + nota2 + nota3) / 3
print('Sua média foi: ',  media)

if media == 10:
    print('Aprovado com distinção. Parabéns!!')
elif media >= 7 and media < 10:
    print('Parabéns, você foi aprovado!!')
else:
    print('Você foi reprovado.')