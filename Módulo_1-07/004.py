#a = input('Digite algo: ')
#print('O tipo primitivo desse valor é ', type(a))
#print('Só tem espaços? ', a.isspace())
#print('É um número? ', a.isnumeric())

#nome = input('Qual é o seu nome?')
#print('prazer em te conhecer {:^20}!'.format(nome))

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2 
e = n1 ** n2

print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d))
print('Divisão inteira {} e potência {}'.format(di, e))

#print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end='')