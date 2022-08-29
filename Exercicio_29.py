#Sabe-se que: pé = 12 polegadas; 1 jarda = 3 pés e 1 milha = 1,760 jarda. Faça um programa que receba uma medida em pés, faça as conversões a seguir e mostre os resultados.

pes = float(input('Pés: '))

jarda = pes / 3
polegada = pes * 12
milha = pes / 5280

conversao = (jarda, polegada,  milha)

print(conversao)