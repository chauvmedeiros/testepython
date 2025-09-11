#Escreva um programa que converta uma temperatura digitada em ºC para ºF

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c) / 5) +32
print('A temperatura de {}ºC corresponde a {}°F'.format(c, f))