#Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milimétros. 

n = float(input('Digite o valor do metro:'))
cem = n * 100
mil = n * 1000

print('O valor de {} em centímentros é {:.0f} cm \n O valor em milímetros é {:.0f} ml'.format(n, cem, mil))