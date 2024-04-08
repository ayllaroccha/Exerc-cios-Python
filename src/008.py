# conversor de medidas
medida = float(input('Digite uma distancia em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {} corresponde à {:.6f}km, \n{:.6f}hm, \n{:.6f}dam, \n{:.0f}dm, \n{:.0f}cm e \n{:.0f}mm'.format(medida, km, hm, dam, dm, cm, mm))