
import math
numero = float(input('Número: '))

if numero < 0:
    print('O número não pode ser menor que 0')

quadrado = numero **2
cubo = numero **3
raiz = math.sqrt(numero)

print(quadrado, cubo, raiz)
