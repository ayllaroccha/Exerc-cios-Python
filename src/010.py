# Conversor de moedas
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 5.06
euro = real / 5.48
print('Com R${:.2f} você pode comprar U${:.2f} e ${:.2f}'.format(real, dolar, euro))