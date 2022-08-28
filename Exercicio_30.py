#Escreva um programa que receba como entrada um número de 5 dígitos, separe o número em dígitos individuais e os imprima separados por 3 espaços cada um. Por exemplo, se o usuário digitar 42339, o programa deverá imprimir: 4 2 3 3. 

from calendar import c
from re import M, U
from this import d


numero = int(input('Número: '))

primeiro = numero // 1 % 10
segundo = numero // 10 % 10
terceiro = numero // 100 % 10
quarto = numero // 1000 % 10
quinto = numero // 10000 % 10

print('primeiro: {}' .format(primeiro))
print('segundo: {}' .format(segundo))
print('terceiro: {}' .format(terceiro))
print('quarto: {}' .format(quarto))
print('quinto: {}' .format(quinto))