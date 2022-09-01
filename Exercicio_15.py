#Faça um programa que leia dois números inteiros e imprima o dividendo, divisor, quociente e resto da divisão

dividendo = int(input("Número 1:"))
divisor = int(input('Número 2: '))

quociente = dividendo/divisor

if quociente != 0:
    resto = dividendo % divisor
print(f'Dividendo: {dividendo}, Divisor {divisor}, Quociente {quociente}, Resto {resto}')