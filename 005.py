#Faça um programa que leia um número inteiro 
# e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um valor:'))

#print('O sucessor do seu número é {} e o seu antecessor é {}'.format(sucessor, antecessor))

print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))