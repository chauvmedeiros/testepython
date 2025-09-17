#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento 

salário = float(input('Qual é o seu salário atual?'))
novo = salário + (salário * 15 / 100)
print('Com base no seu salário de R${:.2f}, o seu salário atual com reajuste de 15% será R${:.2f}'.format(salário, novo))