#Faça um programa que receba três notas e seus respectivos pesos, calcule e mostre a média ponderada.

numero_1 = int(input('Número 1: '))
numero_2 = int(input('Número 2: '))
numero_3 = int(input('Número 3: '))
peso_1 = int(input('Peso 1: '))
peso_2 = int(input('Peso 2: '))
peso_3 = int(input('Peso 3: '))

valor = numero_1 / peso_1 + numero_2 / peso_2 + numero_3 / peso_3

print(valor)