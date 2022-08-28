#Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.

numero_1 = int(input('Número 1: '))
numero_2 = int(input('Número 2: '))

elevado =  numero_1 ** numero_2

if (numero_1 or numero_2) > 0:
    print(elevado)
else:
    print('O numero precisa ser maior que zero')