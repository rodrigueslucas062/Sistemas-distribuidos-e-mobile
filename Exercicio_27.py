#Faça um programa que receba um número positivo e maior que zero, calcule e mostre

import math
numero = float(input('Número: '))

if numero > 0:
    quadrado = numero **2
    cubo = numero **3
    raiz = math.sqrt(numero)
else:
    print('O numero precisa ser maior que zero')

print(quadrado, cubo, raiz)