#Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m^2. 

larg = float(input('Qual a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
área = larg * alt
pintura = área / 2

print('A lagura da parede:{} \n Altura da parede:{}'.format(larg, alt))
print('Sua parede tem a dimensão de {}x{} e sua área é de {}'.format(larg, alt, área))
print('Para pintar essa parede, você precisará de {} litros de tinta'.format(pintura))