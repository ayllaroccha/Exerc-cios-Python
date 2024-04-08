# media aritmética
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A media entre {} e {} é igual a {}'.format(n1, n2, media))

# verificar se foi aprovado
if (media >= 7):
    print('Você está aprovado')
else:
    print('Você está reprovado')