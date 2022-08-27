#Escreva um programa que receba como entrada o raio de um círculo e imprima o diâmetro, a circunferência e a área. Para isso, utilize as fórmulas: diâmetro = 2r; circunferência = 2πr, área = πr².

import math
from cmath import pi
from re import match

raio = float(input('Raio: '))

diametro = raio * 2
circunferencia = 2 * math.pi * raio
area = math.pi * raio**2

print(diametro, circunferencia, area)