#Faça um programa que receba dois números maiores que zero, calcule e mostre um elevado ao outro.

numero_1 = int(input('Número 1: '))
numero_2 = int(input('Número 2: '))

if (numero_1, numero_2) > 0:
    elevado =  numero_1 ** numero_2 
else:
    print('O numero precisa ser maior que zero')

print(elevado)