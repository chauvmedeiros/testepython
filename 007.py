#Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média. 

n1 = float(input('Digite sua nota em Português:'))
n2 = float(input('Digite sua nota em Matemática:'))
n3 = float(input('Digite sua nota em Redação:'))
média = (n1 + n2 + n3) / 3

print('A sua média é {}'.format(média))